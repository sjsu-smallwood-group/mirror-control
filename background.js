'use strict'

import { app, protocol, BrowserWindow } from 'electron'
import {
  createProtocol,
  installVueDevtools
} from 'vue-cli-plugin-electron-builder/lib'

const isDevelopment = process.env.NODE_ENV !== 'production'

let win

protocol.registerSchemesAsPrivileged([
  { scheme: 'app', privileges: { secure: true, standard: true } }
])

function createWindow () {
  win = new BrowserWindow({ width: 800, height: 600, webPreferences: { nodeIntegration: true }})

  if (process.env.WEBPACK_DEV_SERVER_URL) {
    win.loadURL(process.env.WEBPACK_DEV_SERVER_URL)
   // if (!process.env.IS_TEST) win.webContents.openDevTools()
  } else {
    createProtocol('app')
    win.loadURL('app://./index.html')
  }

  win.on('closed', () => {
    win = null
  })
}

app.on('activate', () => {
  if (win === null) createWindow()
})

app.on('ready', async () => {
  
  //if (isDevelopment && !process.env.IS_TEST) {
  //  try {
  //    await installVueDevtools()
  //  } catch (e) {
  //    console.error('Vue Devtools failed to install:', e.toString())
  //  }
 // }
  createWindow()
})

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit()
  }
})
