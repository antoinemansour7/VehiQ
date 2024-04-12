module.exports = {
  preset: '@vue/cli-plugin-unit-jest/presets/no-babel',
  moduleNameMapper: {
    '^@/(.*)$': '<rootDir>/frontendvue/src/$1', // Adjust this based on your actual folder structure
    '^@views/(.*)$': '<rootDir>/frontendvue/src/views/$1', // Add mapping for @views alias
    '^axios$': '<rootDir>/frontendvue/node_modules/axios', // Add this line to handle axios module resolution
  },
  transform: {
    '^.+\\.js$': 'babel-jest',
  },
};
