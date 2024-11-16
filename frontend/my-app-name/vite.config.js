import react from '@vitejs/plugin-react';
import { defineConfig } from 'vite';

export default defineConfig({
  base: '/static/frontend/', // Django STATIC_URL과 일치
  plugins: [react()],
});
