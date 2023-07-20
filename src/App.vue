<template>
  <div id="app">
    <h1>Dual Mirror Synchronization System</h1>
    <div class="motor-wrapper">
      <div class="motor" v-for="motor in [{id:'MotorA', name: 'Motor A'}, {id:'MotorB', name: 'Motor B'}]" :key="motor.id">
    <h2>{{ motor.name }}</h2>
    <div class="axis-wrapper">
      <div class="axis x-axis">
        <input type="range" min="0" max="264200" v-model="sliders[motor.id].x" class="slider" @input="showHelpMessage( motor.name + ' X axis max screw turns 264200')">
        <input type="number" min="0" max="264200" v-model="sliders[motor.id].x" class="value-box" @input="showHelpMessage( motor.name + ' X axis max screw turns 264200')">
      </div>
      <div class="axis y-axis">
        <input type="range" min="0" max="264200" v-model="sliders[motor.id].y" class="slider vertical" @input="showHelpMessage ( motor.name + ' Y axis max screw turns 264200')" >
        <input type="number" min="0" max="264200" v-model="sliders[motor.id].y" class="value-box" @input="showHelpMessage ( motor.name + ' Y axis max screw turns 264200')">
      </div>
    </div>
   </div>
    </div>
    <button @click="sendToArduino">Send to Arduino</button>
    <p>&copy; 2023 Smallwood Research Group SJSU</p>
    <div class="help-message" v-if="dBoolShowHelpMessage" v-html="helpMessage"></div>
  </div>
</template>

<script>
import fs from 'fs'
const path = './slider-values.json';

export default {
  data() {
    return {
      sliders: {
        MotorA: {
          x: 0,
          y: 0
        },
        MotorB: {
          x: 0,
          y: 0
        }
      },
      initialSliders: {
        MotorA: {
          x: 0,
          y: 0
        },
        MotorB: {
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
     
      this.showHelpMessage(`Arduino told: \n
    <b>Motor A:</b> move X axis by ${this.colorNumber(this.sliders.MotorA.x - this.initialSliders.MotorA.x)}, 
    Y axis by ${this.colorNumber(this.sliders.MotorA.y - this.initialSliders.MotorA.y)} \n
    <b>Motor B:</b> move X axis by ${this.colorNumber(this.sliders.MotorB.x - this.initialSliders.MotorB.x)}, 
    Y axis by ${this.colorNumber(this.sliders.MotorB.y - this.initialSliders.MotorB.y)}`); 
      
      
      this.saveSliders();
    },
    initSliders() {
      if (fs.existsSync(path)) {
        const data = fs.readFileSync(path, 'utf8');
        this.sliders = JSON.parse(data);
        this.initialSliders = JSON.parse(data);
      }
    },
    saveSliders() {
      console.log('writing')
      const data = JSON.stringify(this.sliders);
      fs.writeFileSync(path, data);
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
