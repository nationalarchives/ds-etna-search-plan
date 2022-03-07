const path = require('path');

module.exports = {
  mode: 'development',
  devtool: false,
  entry: './static/js/src/search.js',
  output: {
    filename: 'search.js',
    path: path.resolve(__dirname, './static/js/dist'),
  },
  module: {
  rules: [
    {
      test: /\.m?js$/,
      exclude: /(node_modules|bower_components)/,
      use: {
        loader: 'babel-loader',
        options: {
          presets: ['@babel/preset-env']
        }
      }
    }
  ]
},
target: ['web', 'es5']
};