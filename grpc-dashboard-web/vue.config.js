
import { defineConfig } from '@vue/cli-service'

export default defineConfig({
    devServer: {
        proxy: {
          '/': {
            target: 'http://localhost:5050/',
            changeOrigin: true
          }
        }
      }
})