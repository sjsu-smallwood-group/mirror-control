# How to run this app on mac?

This app has been tested on node version 16
Make sure node version 20 is running with the command

> node -v

It is recommended to use nvm [node version manager] to manage node versions.

> nvm list
> nvm use 16

```
# Step 1/2: Installing dependencies:

> yarn install
If you do not have yarn installed, you can install it with the command:
> npm install -g yarn
If you do not have node:
> brew install node

# Step 2/2: Running the app:

> yarn electron:serve
```

# Current issues

1. App does not run on Node 18 or 20. I get the error:

vk-tech@vk-primary-desktop-mac-mini ~/D/h/m/gui-js (main) [SIGINT]> nvm use 18
Now using Node v18.17.0 (npm 9.6.7) ~/.local/share/nvm/v18.17.0/bin/node
vk-tech@vk-primary-desktop-mac-mini ~/D/h/m/gui-js (main)> yarn electron:serve
yarn run v1.22.19
$ vue-cli-service electron:serve
INFO Starting development server...
10% building 2/2 modules 0 activeError: error:0308010C:digital envelope routines::unsupported
at new Hash (node:internal/crypto/hash:69:19)
at Object.createHash (node:crypto:133:10)
at module.exports (/Users/vk-tech/Documents/ha/mirror-control/gui-js/node_modules/webpack/lib/util/createHash.js:135:53)
at NormalModule.\_initBuildHash (/Users/vk-tech/Documents/ha/mirror-control/gui-js/node_modules/webpack/lib/NormalModule.js:417:16)
at handleParseError (/Users/vk-tech/Documents/ha/mirror-control/gui-js/node_modules/webpack/lib/NormalModule.js:471:10)
at /Users/vk-tech/Documents/ha/mirror-control/gui-js/node_modules/webpack/lib/NormalModule.js:503:5
at /Users/vk-tech/Documents/ha/mirror-control/gui-js/node_modules/webpack/lib/NormalModule.js:358:12
at /Users/vk-tech/Documents/ha/mirror-control/gui-js/node_modules/loader-runner/lib/LoaderRunner.js:373:3
at iterateNormalLoaders (/Users/vk-tech/Documents/ha/mirror-control/gui-js/node_modules/loader-runner/lib/LoaderRunner.js:214:10)
at iterateNormalLoaders (/Users/vk-tech/Documents/ha/mirror-control/gui-js/node_modules/loader-runner/lib/LoaderRunner.js:221:10)
at /Users/vk-tech/Documents/ha/mirror-control/gui-js/node_modules/loader-runner/lib/LoaderRunner.js:236:3
at runSyncOrAsync (/Users/vk-tech/Documents/ha/mirror-control/gui-js/node_modules/loader-runner/lib/LoaderRunner.js:130:11)
at iterateNormalLoaders (/Users/vk-tech/Documents/ha/mirror-control/gui-js/node_modules/loader-runner/lib/LoaderRunner.js:232:2)
at Array.<anonymous> (/Users/vk-tech/Documents/ha/mirror-control/gui-js/node_modules/loader-runner/lib/LoaderRunner.js:205:4)
at Storage.finished (/Users/vk-tech/Documents/ha/mirror-control/gui-js/node_modules/enhanced-resolve/lib/CachedInputFileSystem.js:55:16)
at /Users/vk-tech/Documents/ha/mirror-control/gui-js/node_modules/enhanced-resolve/lib/CachedInputFileSystem.js:91:9
10% building 2/5 modules 3 active /Users/vk-tech/Documents/ha/mirror-control/gui-js/node_modules/webpack/hot/dev-server.jsnode:internal/crypto/hash:69
this[kHandle] = new \_Hash(algorithm, xofLen);
^

Error: error:0308010C:digital envelope routines::unsupported
at new Hash (node:internal/crypto/hash:69:19)
at Object.createHash (node:crypto:133:10)
at module.exports (/Users/vk-tech/Documents/ha/mirror-control/gui-js/node_modules/webpack/lib/util/createHash.js:135:53)
at NormalModule.\_initBuildHash (/Users/vk-tech/Documents/ha/mirror-control/gui-js/node_modules/webpack/lib/NormalModule.js:417:16)
at handleParseError (/Users/vk-tech/Documents/ha/mirror-control/gui-js/node_modules/webpack/lib/NormalModule.js:471:10)
at /Users/vk-tech/Documents/ha/mirror-control/gui-js/node_modules/webpack/lib/NormalModule.js:503:5
at /Users/vk-tech/Documents/ha/mirror-control/gui-js/node_modules/webpack/lib/NormalModule.js:358:12
at /Users/vk-tech/Documents/ha/mirror-control/gui-js/node_modules/loader-runner/lib/LoaderRunner.js:373:3
at iterateNormalLoaders (/Users/vk-tech/Documents/ha/mirror-control/gui-js/node_modules/loader-runner/lib/LoaderRunner.js:214:10)
at Array.<anonymous> (/Users/vk-tech/Documents/ha/mirror-control/gui-js/node_modules/loader-runner/lib/LoaderRunner.js:205:4)
at Storage.finished (/Users/vk-tech/Documents/ha/mirror-control/gui-js/node_modules/enhanced-resolve/lib/CachedInputFileSystem.js:55:16)
at /Users/vk-tech/Documents/ha/mirror-control/gui-js/node_modules/enhanced-resolve/lib/CachedInputFileSystem.js:91:9
at /Users/vk-tech/Documents/ha/mirror-control/gui-js/node_modules/graceful-fs/graceful-fs.js:123:16
at FSReqCallback.readFileAfterClose [as oncomplete] (node:internal/fs/read_file_context:68:3) {
opensslErrorStack: [ 'error:03000086:digital envelope routines::initialization error' ],
library: 'digital envelope routines',
reason: 'unsupported',
code: 'ERR_OSSL_EVP_UNSUPPORTED'
}

Node.js v18.17.0
error Command failed with exit code 1.
info Visit https://yarnpkg.com/en/docs/cli/run for documentation about this command.
