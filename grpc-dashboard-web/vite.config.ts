import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import vueJsx from '@vitejs/plugin-vue-jsx'
import VueDevTools from 'vite-plugin-vue-devtools'
import commonjs from 'vite-plugin-commonjs';
import vitePluginRequire from "vite-plugin-require";
// import path from 'path';

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    vue(),
    commonjs(),
    // vueJsx(),
    // VueDevTools(),
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url)),
      // 'google-protobuf': path.resolve(__dirname, 'node_modules/google-protobuf'),
    }
  },
  build: {
    commonjsOptions: { transformMixedEsModules: true } // Change
  }
  
})
