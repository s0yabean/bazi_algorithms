// Used for extending classes from the default in tailwind.css
// rebuild command: npx tailwindcss build src/css/styles.css -o src/css/tailwind.css
// Minute 7: https://www.youtube.com/watch?v=6UVQlB1eo5A&ab_channel=TheNetNinja
module.exports = {
  purge: [],
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {
      colors: {
        'pc-blue': '#323451',
        'pc-blue-dark': '#1e1f30',
        'pc-gray': '#797A88',
        'pc-brown': '#BFA59C',
        'pc-brown-dark': '#5F524E'
      },
      fontFamily: {
        'hn': ["Helvetica Neue"],
        'cd': ["Condor"]
      }
    },
  },
  variants: {
    extend: {},
  },
  plugins: [],
}
