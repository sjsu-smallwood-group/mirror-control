<template>
  <div id="app">
    <h1>Dual Mirror Synchronization System</h1>
    <div class="mirror-wrapper">
      <div class="mirror" v-for="mirror in ['A', 'B']" :key="mirror">
        <h2>Mirror {{ mirror }}</h2>
        <div class="axis-wrapper">
          <div class="axis x-axis">
            <input type="range" min="0" max="264200" v-model="sliders[mirror].x" class="slider" @input="showHelpMessage">
            <input type="number" min="0" max="264200" v-model="sliders[mirror].x" class="value-box" @input="showHelpMessage">
          </div>
          <div class="axis y-axis">
            <input type="range" min="0" max="264200" v-model="sliders[mirror].y" class="slider vertical" @input="showHelpMessage">
            <input type="number" min="0" max="264200" v-model="sliders[mirror].y" class="value-box" @input="showHelpMessage">
          </div>
        </div>
      </div>
    </div>
    <button @click="sendToArduino">Send to Arduino</button>
    <p>&copy; 2023 Smallwood Research Group SJSU</p>
    <div class="help-message" v-if="dBoolShowHelpMessage">{{helpMessage}}</div>
  </div>
</template>

<script>
import fs from 'fs'
const path = './slider-values.json';

export default {
  data() {
    return {
      sliders: {
        A: {
          x: 0,
          y: 0
        },
        B: {
          x: 0,
          y: 0
        }
      },
      initialSliders: {
        A: {
          x: 0,
          y: 0
        },
        B: {
          x: 0,
          y: 0
        }
      },
      dBoolShowHelpMessage: false

    };
  },
  created() {
    this.initSliders();
  },
  methods: {
    sendToArduino() {
     this.helpMessage = 'Asking arduino to: \n' +
        `1. For mirror A: move X axis by ${this.sliders.A.x - this.initialSliders.A.x} turns forward, ` +
        `Y axis by ${this.sliders.A.y - this.initialSliders.A.y} turns backward \n` +
        `2. For mirror B: move X axis by ${this.sliders.B.x - this.initialSliders.B.x} turns forward, ` +
        `Y axis by ${this.sliders.B.y - this.initialSliders.B.y} turns backward`;
      this.dBoolShowHelpMessage = true;
      // Remove the help message after 3 seconds
      setTimeout(() => {
        this.dBoolShowHelpMessage = false;
      }, 10000);
      this.saveSliders();      this.saveSliders();
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
     showHelpMessage() {
      this.helpMessage = 'This is the number of screw turns. The maximum screw turns for this model is 264,200';
      this.dBoolShowHelpMessage = true;
      // Remove the help message after 3 seconds
      setTimeout(() => {
        this.dBoolShowHelpMessage = false;
      }, 10000);
    },
  },
};
</script>

<style scoped>
h1 {
  text-align: center;
}

.mirror-wrapper {
  display: flex;
  justify-content: space-between;
  margin-bottom: 20px;
}

.mirror {
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
</style>
