const path = require('path');

module.exports = {
  entry: './myangularapp/src/styles.scss',
  output: {
    // Это место, куда будет складываться скомпилированный CSS
    // Важно: Webpack по умолчанию не создает отдельный CSS файл
    // для этого нам понадобится дополнительный плагин
    path: path.resolve(__dirname, 'static/dist'),
  },
  module: {
    rules: [
      {
        test: /\.scss$/,
        use: [
          'style-loader',
          // Переводит CSS в CommonJS
          'css-loader',
          // Компилирует Sass в CSS
          'sass-loader',
        ],
      },
    ],
  },
};
