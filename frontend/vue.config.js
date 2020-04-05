const BundleTracker = require("webpack-bundle-tracker");
const path = require('path')
var debug= true;
module.exports = {
    "transpileDependencies": [
        "vuetify"
    ],


    publicPath: debug?'http://localhost:8080':"/static/dist",
    outputDir: debug?'./dist/':"../static/dist/",

    chainWebpack: config => {

        config.optimization
            .splitChunks(false)

        config
            .plugin('BundleTracker')
            .use(BundleTracker, [{filename: '../frontend/webpack-stats.json'}])

        config.resolve.alias
            .set('__STATIC__', 'static')

        config.devServer
            .public('http://localhost:8080')
            .host('localhost')
            .port(8080)
            .hotOnly(true)
            .watchOptions({poll: 1000})
            .https(false)
            .headers({"Access-Control-Allow-Origin": ["\*"]})
    },
};

