/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "SRC/seo_wireframe/core/templates/**/*.{html,js}",
    "SRC/seo_wireframe/style1/templates/**/*.{html,js}",
    "SRC/seo_wireframe/style2/templates/**/*.{html,js}",
  ],
  theme: {
    extend: {
      colors: {
        "seotur":{
          600: "#2B6982"
        },
        "dashbg":{
          700: "#0369a1"
        }  
      },
    },
  },
  plugins: [],
}

