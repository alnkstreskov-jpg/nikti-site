/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./*.html"],
  theme: {
    extend: {
      colors: {
        "y2k-blue": "#0033cc",
        "y2k-magenta": "#ff00cc",
        "y2k-yellow": "#fff000"
      },
      fontFamily: {
        syne: ["Unbounded", "sans-serif"],
        inter: ["Inter", "sans-serif"]
      },
      boxShadow: {
        brutal: "4px 4px 0 0 rgba(0, 0, 0, 1)",
        "brutal-lg": "8px 8px 0 0 rgba(0, 0, 0, 1)"
      }
    }
  },
  plugins: []
};
