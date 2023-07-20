<template>
  <div id="app">
    <h1>Dual Mirror Synchronization System</h1>
    <div class="mirror-wrapper">
      <div class="mirror" v-for="mirror in ['A', 'B']" :key="mirror">
        <h2>Mirror {{ mirror }}</h2>
        <div class="axis-wrapper">
          <div class="axis x-axis">
            <input type="range" min="-100" max="100" v-model="sliders[mirror].x" class="slider">
            <input type="number" min="-100" max="100" v-model="sliders[mirror].x" class="value-box">
          </div>
          <div class="axis y-axis">
            <input type="range" min="-100" max="100" v-model="sliders[mirror].y" class="slider vertical">
            <input type="number" min="-100" max="100" v-model="sliders[mirror].y" class="value-box">
          </div>
        </div>
      </div>
    </div>
    <button @click="sendToArduino">Send to Arduino</button>
    <p>&copy; 2023 Smallwood Research Group SJSU</p>
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
          x: 100,
          y: 100
        },
        B: {
          x: 100,
          y: 100
        }
      }
    };
  },
  created() {
    this.initSliders();
  },
  methods: {
    sendToArduino() {
      console.log('Sending values to Arduino:', this.sliders);
      // Implement your functionality here
      this.saveSliders();
    },
    initSliders() {
      if (fs.existsSync(path)) {
        const data = fs.readFileSync(path, 'utf8');
        this.sliders = JSON.parse(data);
      }
    },
    saveSliders() {
      console.log('writing')
      const data = JSON.stringify(this.sliders);
      fs.writeFileSync(path, data);
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
  width: 60px;
}
</style>
