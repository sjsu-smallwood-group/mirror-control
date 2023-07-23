<template>
  <div id="app">
    <h1>Dual Mirror Synchronization System</h1>
    <div class="motor-wrapper">
      <div class="motor" v-for="motor in [{id:'Motor1', name: 'Motor 1'}, {id:'Motor2', name: 'Motor 2'}]" :key="motor.id">
    <h2>{{ motor.name }}</h2>
    <div class="axis-wrapper">
      <div class="axis x-axis">
        <input type="range" min="0" max="264200" v-model="sliders[motor.id].x" class="slider" @input="showHelpMessage( motor.name + ' X axis Screw turns. Max: 264,200. Initial: ' + formatNumber(initialSliders[motor.id].x) + '. Planned: ' + formatNumber(sliders[motor.id].x - initialSliders[motor.id].x))">
        <input type="number" min="0" max="264200" v-model="sliders[motor.id].x" class="value-box" @input="showHelpMessage( motor.name + ' X axis Screw turns. Max: 264,200. Initial: ' + formatNumber(initialSliders[motor.id].x)+ '. Planned: ' + formatNumber(sliders[motor.id].x - initialSliders[motor.id].x))">
      </div>
      <div class="axis y-axis">
        <input type="range" min="0" max="264200" v-model="sliders[motor.id].y" class="slider vertical" @input="showHelpMessage ( motor.name + ' Y axis Screw turns. Max: 264,200. Initial: ' + formatNumber(initialSliders[motor.id].y)+ '. Planned: ' + formatNumber(sliders[motor.id].y - initialSliders[motor.id].y))">
        <input type="number" min="0" max="264200" v-model="sliders[motor.id].y" class="value-box" @input="showHelpMessage ( motor.name + ' Y axis Screw turns. Max: 264,200. Initial: ' + formatNumber(initialSliders[motor.id].y) + '. Planned: ' + formatNumber(sliders[motor.id].y - initialSliders[motor.id].y))">
      </div>
    </div>
   </div>
   </div>
   <div class="experiment-details">
    <label>Experimenter:
        <select v-model="experimentDetails.experimenter">
            <option value="Hediye">Hediye</option>
            <option value="Ayne">Ayne</option>
            <option value="Prof. Smallwood">Prof. Smallwood</option>
        </select>
    </label>
    <label>Element:
        <select v-model="experimentDetails.element">
            <option value="MoS2_on_SiO2">MoS2 on SiO2</option>
            <option value="silver">Silver</option>
            <option value="gold">Gold</option>
        </select>
    </label>
    <label>Temperature (K):
        <input type="number" min="0" step="0.01" v-model="experimentDetails.temperature">
    </label>
</div>
    <button @click="sendToArduino">Send to Arduino</button>
    <p>&copy; 2023 Smallwood Research Group SJSU</p>
    <div class="help-message" v-if="dBoolShowHelpMessage" v-html="helpMessage"></div>
  </div>
</template>

<script>
import sqlite3 from 'sqlite3';
const db = new sqlite3.Database('../experiments-notebook.sqlite');
console.log(db)

export default {
  data() {
    return {
      
      sliders: {
        Motor1: {
          x: 0,
          y: 0
        },
        Motor2: {
          x: 0,
          y: 0
        }
      },
        experimentDetails: {
      experimenter: 'Hediye',  // default value
      element: 'MoS2_on_SiO2',  // default value
      temperature: 0
    },
      initialSliders: {
        Motor1: {
          x: 0,
          y: 0
        },
        Motor2: {
          x: 0,
          y: 0
        }
      },
      dBoolShowHelpMessage: false,
      helpMessage:'',
      helpMessageTimeout: null, // for keeping track of the timer. If this help message is being shown on the screen "This is the number of screw turns. The maximum screw turns for this model is 264,200" and I click on "Send to Arduino" then the help message from sendToArduino message should come right away
    };
  },
  created() {
    this.initSliders();
  },
  methods: {
    sendToArduino() {
     
      let helpMessage = 'Arduino told to turn screws: \n';

      // Check if each value is non-zero before adding it to the help message
      if (this.sliders.Motor1.x - this.initialSliders.Motor1.x !== 0) {
        helpMessage += `<b>Motor 1:</b> X: ${this.colorNumber(this.sliders.Motor1.x - this.initialSliders.Motor1.x)}\n`;
      }
      if (this.sliders.Motor1.y - this.initialSliders.Motor1.y !== 0) {
        helpMessage += `<b>Motor 1:</b> Y: ${this.colorNumber(this.sliders.Motor1.y - this.initialSliders.Motor1.y)}\n`;
      }
      if (this.sliders.Motor2.x - this.initialSliders.Motor2.x !== 0) {
        helpMessage += `<b>Motor 2:</b> X: ${this.colorNumber(this.sliders.Motor2.x - this.initialSliders.Motor2.x)}\n`;
      }
      if (this.sliders.Motor2.y - this.initialSliders.Motor2.y !== 0) {
        helpMessage += `<b>Motor 2:</b> Y: ${this.colorNumber(this.sliders.Motor2.y - this.initialSliders.Motor2.y)}\n`;
      }

      // Display the help message, if it has any non-zero values
      if (helpMessage !== 'Arduino told to turn screws: \n') {
        this.showHelpMessage(helpMessage); 
      }
          
      this.saveSliders();
    },


    
    initSliders() {
      const selectLastRowSql = "SELECT * FROM tblObservations ORDER BY dateTimeUpdated DESC LIMIT 1";

        console.log(selectLastRowSql);

        db.get(selectLastRowSql, (err, row) => {
          console.log(row);
          if (row) {
            this.sliders.Motor1.x = row.motor1_abs_X;
            this.sliders.Motor1.y = row.motor1_abs_Y;
            this.sliders.Motor2.x = row.motor2_abs_X;
            this.sliders.Motor2.y = row.motor2_abs_Y;
            
            this.initialSliders.Motor1.x = row.motor1_abs_X;
            this.initialSliders.Motor1.y = row.motor1_abs_Y;
            this.initialSliders.Motor2.x = row.motor2_abs_X;
            this.initialSliders.Motor2.y = row.motor2_abs_Y;
          }
        });
    },
    
    saveSliders() {
      const dateTimeUpdated = new Date().toISOString();
        const { x: Motor1_X, y: Motor1_Y } = this.sliders.Motor1;
        const { x: Motor2_X, y: Motor2_Y } = this.sliders.Motor2;

        const insertRowSql = `INSERT INTO tblObservations(dateTimeUpdated, Motor1_abs_X, Motor1_abs_Y, Motor2_abs_X, Motor2_abs_Y,material, experiementRanBy, temperature_kelvin) VALUES('${dateTimeUpdated}', ${Motor1_X}, ${Motor1_Y}, ${Motor2_X}, ${Motor2_Y},
      '${this.experimentDetails.element}',
      '${this.experimentDetails.experimenter}',
      ${this.experimentDetails.temperature})`;

        console.log(insertRowSql);

        db.run(
          insertRowSql,
          (err) => {
            if (err) {
              console.error(err.message);
            }
          }
        );
        // set the initial values to the current values
        this.initialSliders.Motor1.x = Motor1_X;
        this.initialSliders.Motor1.y = Motor1_Y;
        this.initialSliders.Motor2.x = Motor2_X;
        this.initialSliders.Motor2.y = Motor2_Y;    
    },
       
    showHelpMessage(newMessage) {
      this.helpMessage = newMessage;
      this.dBoolShowHelpMessage = true;
      // Clear any existing timers
      if (this.helpMessageTimeout) {
        clearTimeout(this.helpMessageTimeout);
      }
      // Set a new timer
      this.helpMessageTimeout = setTimeout(() => {
        this.dBoolShowHelpMessage = false;
      }, 10000);
    },
    formatNumber(num) {
      return num.toLocaleString();
    },
    colorNumber(num) {
      return `<span class='${num >= 0 ? 'positive' : 'negative'}'>${this.formatNumber(num)}</span>`;
    },
  },
};
</script>

<style scoped>
h1 {
  text-align: center;
}

.motor-wrapper {
  display: flex;
  justify-content: space-between;
  margin-bottom: 20px;
}

.motor {
  flex: 1;
  padding: 0 20px;
}

.axis-wrapper {
  position: relative;
  height: 400px;
  width: 400px;
  margin: auto;
}

.x-axis {
  position: absolute;
  width: 400px;
  left: 0;
  top: 50%;
}

.y-axis {
  position: absolute;
  height: 400px;
  left: 50%;
  top: 0;
}

.slider {
  width: 100%;
}

.slider::-webkit-slider-thumb {
  -webkit-appearance: none;
  appearance: none;
  background: #cccccc;
}

.slider:active::-webkit-slider-thumb {
  background: #cccccc;
}

.slider:focus {
  outline: none;
}

.slider:focus::-webkit-slider-thumb {
  background: #cccccc;
}

.vertical {
  -webkit-appearance: slider-vertical; /* Webkit */
  width: 8px;
  height: 100%;
  padding: 0 5px;
}

button {
  display: block;
  margin: 20px auto;
  padding: 10px 20px;
  background-color: #4CAF50; /* Green */
  border: none;
  color: white;
  text-align: center;
  text-decoration: none;
  font-size: 16px;
  transition-duration: 0.4s;
  cursor: pointer;
}

button:hover {
  background-color: #45a049;
}

.value-box {
  border: 1px solid #ccc;
  padding: 5px;
  width: 90px;
}
.help-message {
    position: absolute;
    bottom: 0;
    width: 100%;
    height: 50px;
    line-height: 50px;
    text-align: center;
    background-color: #e0e0e0;
    color: #495057;
  }
.positive {
  color: green;
}

.negative {
  color: red;
}
</style>
