// Used for extending classes from the default in tailwind.css
// rebuild command: npx tailwindcss build src/css/styles.css -o src/css/tailwind.css
// Minute 7: https://www.youtube.com/watch?v=6UVQlB1eo5A&ab_channel=TheNetNinja
module.exports = {
  purge: [],
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {
      colors: {
        'theme-l-green': '#CCF5AC',
        'theme-d-green': '#223127',
      }
    },
  },
  variants: {
    extend: {},
  },
  plugins: [],
}
