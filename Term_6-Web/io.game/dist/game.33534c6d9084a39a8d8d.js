/*
 * ATTENTION: The "eval" devtool has been used (maybe by default in mode: "development").
 * This devtool is neither made for production nor for readable output files.
 * It uses "eval()" calls to create a separate source file in the browser devtools.
 * If you are trying to read the output file, select a different devtool (https://webpack.js.org/configuration/devtool/)
 * or disable the default devtool with "devtool: false".
 * If you are looking for production-ready output files, see mode: "production" (https://webpack.js.org/configuration/mode/).
 */
/******/ (() => { // webpackBootstrap
/******/ 	var __webpack_modules__ = ({

/***/ "./client/css/styles.css":
/*!*******************************!*\
  !*** ./client/css/styles.css ***!
  \*******************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

"use strict";
eval("__webpack_require__.r(__webpack_exports__);\n// extracted by mini-css-extract-plugin\n\n\n//# sourceURL=webpack:///./client/css/styles.css?");

/***/ }),

/***/ "./client/index.js":
/*!*************************!*\
  !*** ./client/index.js ***!
  \*************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

"use strict";
eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export */ __webpack_require__.d(__webpack_exports__, {\n/* harmony export */   \"canvasWidth\": () => (/* binding */ canvasWidth),\n/* harmony export */   \"canvasHeight\": () => (/* binding */ canvasHeight)\n/* harmony export */ });\n/* harmony import */ var _css_styles_css__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @css/styles.css */ \"./client/css/styles.css\");\n/* harmony import */ var _networking__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./networking */ \"./client/networking.js\");\n/* harmony import */ var _input__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./input */ \"./client/input.js\");\n/* harmony import */ var _render__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ./render */ \"./client/render.js\");\n/* harmony import */ var _leaderboard__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! ./leaderboard */ \"./client/leaderboard.js\");\n\n\n\n\n\n\n\nconst login_menu = document.getElementById('Login_menu');\nconst registration_menu = document.getElementById('Registration_menu');\nconst logged_menu = document.getElementById('logged_in-menu');\nconst changePassword_menu = document.getElementById('change_password_menu');\n\nconst go_signup_btn = document.getElementById('go-signup-btn');\ngo_signup_btn.addEventListener('click', goSignup);\n\nconst go_login_btn = document.getElementById('go-login-btn');\ngo_login_btn.addEventListener('click', goLogin);\n\nfunction goSignup(event) {\n    setTimeout(() => {\n        login_menu.classList.add('hidden');\n        registration_menu.classList.remove('hidden');\n    }, 200);\n}\n\nfunction goLogin(event) {\n    setTimeout(() => {\n        login_menu.classList.remove('hidden');\n        registration_menu.classList.add('hidden');\n    }, 200);\n}\n\n\n// registration handling\nconst registration_form = document.getElementById('registration-form');\nregistration_form.addEventListener('submit', registerUser);\nconst usernameError_registration = document.querySelector('.username.error');\nconst passwordError_registration = document.querySelector('.password.error');\nconst successRegister = document.querySelector('.register.success');\n\n\nfunction cleanErrors_registration() {\n    usernameError_registration.textContent = '';\n    passwordError_registration.textContent = '';\n    successRegister.textContent = '';\n}\n\n\nasync function registerUser(event){\n    event.preventDefault();\n    const username = document.getElementById('register_username').value;\n    const password = document.getElementById('register_password').value;\n    cleanErrors_registration();\n\n    try{\n        const result = await fetch('/api/register', {\n            method: 'POST',\n            headers: {'Content-Type': 'application/json'},\n            body: JSON.stringify({username: username, password: password})\n        }).then((res) => res.json());\n\n        if (result.status === 'ok') {\n            successRegister.textContent = `${username} successfully registered!`;\n        }\n        else {\n            usernameError_registration.textContent = result.error.username;\n            passwordError_registration.textContent = result.error.password;\n        }\n    }\n    catch (e){\n        console.log('Error in registration: ', e);\n    }\n}\n\n\n// login handling\nconst login_form = document.getElementById('login-form');\nlogin_form.addEventListener('submit', loginUser);\nconst usernameError_login = document.querySelector('.usernameLogin.error');\nconst passwordError_login = document.querySelector('.passwordLogin.error');\nconst successLogin = document.querySelector('.login.success');\n\nconst changePassword_btn = document.getElementById('go_change_password');\nchangePassword_btn.addEventListener('click', changePasswordOn);\n\nfunction changePasswordOn(event) {\n    changePassword_menu.classList.remove('hidden');\n    changePassword_btn.classList.add('disabled');\n}\n\n\nfunction cleanErrors_login() {\n    usernameError_login.textContent = '';\n    passwordError_login.textContent = '';\n    successRegister.textContent = '';\n}\n\n\nconst logged_username = document.getElementById('logged_username');\nconst logged_maxScore = document.getElementById('logged_maxScore');\n\nlet isLogged = false;\nlet usernameLogged = '';\n\n\nasync function loginUser(event){\n    event.preventDefault();\n    const username = document.getElementById('login_username').value;\n    const password = document.getElementById('login_password').value;\n\n    try {\n        cleanErrors_login();\n        const result = await fetch('/api/login', {\n            method: 'POST',\n            headers: {\n                'Content-Type': 'application/json'\n            },\n            body: JSON.stringify({\n                username,\n                password\n            })\n        }).then((res) => res.json());\n\n        if (result.status === 'ok') {\n            successLogin.textContent = \"Login successful\";\n            setTimeout(() => {\n                login_menu.classList.add('hidden');\n                logged_menu.classList.remove('hidden');\n                logged_username.textContent = result.data.username;\n                logged_maxScore.textContent = result.data.maxScore;\n                isLogged = true;\n                usernameLogged = result.data.username;\n\n            }, 1000);\n        } else {\n            usernameError_login.textContent = result.error.username;\n            passwordError_login.textContent = result.error.password;\n        }\n    }\n    catch (e){\n        console.log('Error in login: ', e);\n    }\n}\n\nconst changePassword_form = document.getElementById('change_password-form');\nchangePassword_form.addEventListener('submit', changePassword);\n\nconst changePasswordSuccess = document.querySelector('.changePassword.success');\nconst oldPasswordError = document.querySelector('.oldPassword.error');\nconst newPasswordError = document.querySelector('.newPassword.error');\n\nfunction cleanErrorPassword() {\n    oldPasswordError.textContent = '';\n    newPasswordError.textContent = '';\n}\n\nasync function changePassword(event){\n    event.preventDefault();\n    const oldPassword = document.getElementById('old_password').value;\n    const newPassword = document.getElementById('new_password').value;\n\n    cleanErrorPassword();\n\n    const result = await fetch('/api/change-password', {\n        method: 'POST',\n        headers: {\n            'Content-Type': 'application/json'\n        },\n        body: JSON.stringify({\n            oldPassword: oldPassword,\n            newPassword: newPassword,\n        })\n    }).then((res) => res.json());\n\n    if (result.status === 'ok') {\n        changePasswordSuccess.textContent = 'Password changed successful';\n        setTimeout(() => {\n            changePassword_menu.classList.add('hidden');\n        }, 200);\n    }\n    else {\n        console.log(result.error);\n        oldPasswordError.textContent = result.error.oldPassword;\n        newPasswordError.textContent = result.error.newPassword;\n    }\n}\n\n\n\nconst logout_btn = document.getElementById('logout-btn');\nlogout_btn.addEventListener('click', logout);\n\nasync function logout(event) {\n    try{\n        const result = await fetch('/api/logout', {\n            method: 'GET',\n            headers: { 'Content-Type': 'application/json'}\n        }).then(res => res.json());\n        isLogged = false;\n        window.location.reload(true);\n    }\n\n    catch (e) {\n        console.log('Error in logout: ', e);\n    }\n}\n\n\nconst canvas = document.querySelector('canvas');\nconst playButton = document.getElementById('play-button');\nconst noConnectionButton = document.getElementById('no-connect-button');\nconst noConnectModal = document.getElementById('no-connect-modal');\nconst playMenu = document.getElementById('play-menu');\nconst usernameInput = document.getElementById('username-input');\nconst leaderboard = document.getElementById('leaderboard');\nconst deadMenu = document.getElementById('dead-menu');\nconst deadButton = document.getElementById('dead-button');\n\nconst upgradeMenu = document.getElementById('upgrade-menu');\nconst authMenu = document.getElementById('auth');\n\ncanvas.width = window.innerWidth;\ncanvas.height = window.innerHeight;\nvar canvasWidth = canvas.width;\nvar canvasHeight = canvas.height;\n\n\nPromise.all([(0,_networking__WEBPACK_IMPORTED_MODULE_1__.connect)(onGameOver)])\n    .then(() => {\n        playMenu.classList.remove('hidden');\n        usernameInput.focus();\n        playButton.onclick = () => {playClicked()}\n    })\n    .catch(() => {\n        noConnectModal.classList.remove('hidden')\n        noConnectionButton.onclick = () => {\n            window.location.reload();\n        }\n    })\n\n\nfunction playClicked() {\n    playMenu.classList.add('hidden');\n    canvas.classList.remove('hidden');\n    upgradeMenu.classList.remove('hidden');\n    const player_data = {\n        gameUsername: usernameInput.value,\n        isLogged: isLogged,\n        usernameLogged: usernameLogged\n    }\n    console.log(player_data.usernameLogged);\n    (0,_networking__WEBPACK_IMPORTED_MODULE_1__.play)(player_data);\n    (0,_input__WEBPACK_IMPORTED_MODULE_2__.startCapturingInput)();\n    (0,_leaderboard__WEBPACK_IMPORTED_MODULE_4__.setLeaderboardHidden)(false);\n    authMenu.classList.add('hidden');\n\n    // start rendering 100 ms later\n    // so bcs waiting first update from server\n    setTimeout(() => {\n        (0,_render__WEBPACK_IMPORTED_MODULE_3__.startRendering)();\n    }, 100);\n}\n\n\nfunction onGameOver(aliveData) {\n\n    const score = aliveData.score;\n    const prev_score = logged_maxScore.textContent;\n\n    if (score > prev_score) {\n        logged_maxScore.textContent = score;\n    }\n\n    (0,_input__WEBPACK_IMPORTED_MODULE_2__.stopCapturingInput)();\n    (0,_render__WEBPACK_IMPORTED_MODULE_3__.stopRendering)();\n    (0,_leaderboard__WEBPACK_IMPORTED_MODULE_4__.setLeaderboardHidden)(true);\n    canvas.classList.add('hidden');\n    upgradeMenu.classList.add('hidden');\n    deadMenu.classList.remove('hidden');\n    deadButton.onclick = () => {\n        deadMenu.classList.add('hidden');\n        playMenu.classList.remove('hidden');\n        authMenu.classList.remove('hidden');\n    }\n}\n\n//# sourceURL=webpack:///./client/index.js?");

/***/ }),

/***/ "./client/input.js":
/*!*************************!*\
  !*** ./client/input.js ***!
  \*************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

"use strict";
eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export */ __webpack_require__.d(__webpack_exports__, {\n/* harmony export */   \"mouseX\": () => (/* binding */ mouseX),\n/* harmony export */   \"mouseY\": () => (/* binding */ mouseY),\n/* harmony export */   \"startCapturingInput\": () => (/* binding */ startCapturingInput),\n/* harmony export */   \"stopCapturingInput\": () => (/* binding */ stopCapturingInput)\n/* harmony export */ });\n/* harmony import */ var _networking__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./networking */ \"./client/networking.js\");\n/* harmony import */ var _index__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./index */ \"./client/index.js\");\n\n\n\n\n\n\n\n\n\n\n\nconst damageAdd_btn = document.getElementById('dmgUp-btn');\nconst damageDec_btn = document.getElementById('dmgDec-btn');\nconst healthAdd_btn = document.getElementById('health-btn');\nconst regenAdd_btn = document.getElementById('regen-btn');\nconst rangeAdd_btn = document.getElementById('range-btn');\nconst speedAdd_btn = document.getElementById('speed-btn');\nconst reloadAdd_btn = document.getElementById('reload-btn');\nconst upgrade_menu = document.getElementById('upgrade-menu');\n\nconst canvas = document.querySelector('canvas')\n\nvar mouseX = 0;\nvar mouseY = 0;\n\nlet mouseUp = true;\nlet button_pressed = false;\n\n\nfunction onMouseMove(event) {\n    mouseX = event.clientX;\n    mouseY = event.clientY;\n    handleMove(mouseX, mouseY);\n}\n\nfunction onMouseDown(event) {\n    mouseUp = false;\n    if (button_pressed){\n        button_pressed = false;\n        return;\n    }\n\n    let shoot_int = setInterval(() => {\n        const dir = Math.atan2(mouseY - _index__WEBPACK_IMPORTED_MODULE_1__.canvasHeight / 2, mouseX - _index__WEBPACK_IMPORTED_MODULE_1__.canvasWidth / 2);\n        (0,_networking__WEBPACK_IMPORTED_MODULE_0__.createBullet)(dir)\n        if (mouseUp) {\n            clearInterval(shoot_int);\n        }\n    }, 100)\n\n}\n\n\nfunction onMouseUp(event) {\n    mouseUp = true;\n}\n\n\nfunction handleMove(x, y) {\n    const angle = Math.atan2(y - _index__WEBPACK_IMPORTED_MODULE_1__.canvasHeight / 2, x - _index__WEBPACK_IMPORTED_MODULE_1__.canvasWidth / 2);\n    const update_data = {\n        dir: angle,\n        vel_mid: {\n            x: mouseX - window.innerWidth / 2,\n            y: mouseY - window.innerHeight / 2\n        }\n    }\n    ;(0,_networking__WEBPACK_IMPORTED_MODULE_0__.updateDirection)(update_data);\n}\n\n\n// listen for upgrade\nfunction onMenuClicked(event){\n    button_pressed = true;\n}\n\nfunction onDamageAdd(){\n    (0,_networking__WEBPACK_IMPORTED_MODULE_0__.addDamage)('damage_add');\n}\n\nfunction onDamageDec(){\n    (0,_networking__WEBPACK_IMPORTED_MODULE_0__.decDamage)('damage_decrease');\n}\n\nfunction onReloadAdd(){\n    (0,_networking__WEBPACK_IMPORTED_MODULE_0__.addReload)('reload');\n}\n\nfunction onRangeAdd(){\n    (0,_networking__WEBPACK_IMPORTED_MODULE_0__.addRange)('range');\n}\n\nfunction onRegenADd(){\n    (0,_networking__WEBPACK_IMPORTED_MODULE_0__.addRegen)('regen');\n}\n\nfunction onHealthAdd(){\n    (0,_networking__WEBPACK_IMPORTED_MODULE_0__.addHealth)('health');\n}\n\nfunction onSpeedAdd(){\n    (0,_networking__WEBPACK_IMPORTED_MODULE_0__.addSpeed)('speed');\n}\n\n\nfunction startCapturingInput() {\n    window.addEventListener('mousemove', onMouseMove);\n    window.addEventListener('mouseup', onMouseUp);\n    window.addEventListener('mousedown', onMouseDown);\n\n\n    upgrade_menu.addEventListener('click', onMenuClicked);\n    damageAdd_btn.addEventListener('click', onDamageAdd);\n    damageDec_btn.addEventListener('click', onDamageDec);\n    reloadAdd_btn.addEventListener('click', onReloadAdd);\n    rangeAdd_btn.addEventListener('click', onRangeAdd);\n    healthAdd_btn.addEventListener('click', onHealthAdd);\n    regenAdd_btn.addEventListener('click', onRegenADd);\n    speedAdd_btn.addEventListener('click', onSpeedAdd);\n}\n\n\nfunction stopCapturingInput(){\n    window.removeEventListener('mousemove', onMouseMove);\n    window.removeEventListener('mouseup', onMouseUp);\n    window.removeEventListener('mousedown', onMouseDown);\n\n    damageAdd_btn.removeEventListener('click',onDamageAdd);\n    damageDec_btn.removeEventListener('click',onDamageDec);\n    reloadAdd_btn.removeEventListener('click',onReloadAdd);\n    rangeAdd_btn.removeEventListener('click',onRangeAdd);\n    healthAdd_btn.removeEventListener('click',onHealthAdd);\n    regenAdd_btn.removeEventListener('click', onRegenADd);\n    speedAdd_btn.removeEventListener('click',onSpeedAdd);\n}\n\n//# sourceURL=webpack:///./client/input.js?");

/***/ }),

/***/ "./client/leaderboard.js":
/*!*******************************!*\
  !*** ./client/leaderboard.js ***!
  \*******************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

"use strict";
eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export */ __webpack_require__.d(__webpack_exports__, {\n/* harmony export */   \"updateLeaderboard\": () => (/* binding */ updateLeaderboard),\n/* harmony export */   \"setLeaderboardHidden\": () => (/* binding */ setLeaderboardHidden)\n/* harmony export */ });\n/* harmony import */ var lodash_escape__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! lodash/escape */ \"../node_modules/lodash/escape.js\");\n/* harmony import */ var lodash_escape__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(lodash_escape__WEBPACK_IMPORTED_MODULE_0__);\n\n\nconst leaderboard = document.getElementById('leaderboard')\nconst rows = document.querySelectorAll('#leaderboard table tr')\n\nfunction updateLeaderboard(data) {\n\n    const players = data.players;\n    const me_position = data.me_position;\n\n    for(let i = 0; i < players.length; i++) {\n        if (i === me_position){\n            rows[i + 1].innerHTML = `<td bgcolor=\"#F5A3E8\">${i+1}</td><td>${lodash_escape__WEBPACK_IMPORTED_MODULE_0___default()(players[i].username.slice(0, 15))|| 'Noname'}</td><td>${\n                players[i].score\n            }</td>`;\n            continue;\n        }\n        rows[i + 1].innerHTML = `<td>${i+1}</td><td>${lodash_escape__WEBPACK_IMPORTED_MODULE_0___default()(players[i].username.slice(0, 15))|| 'Noname'}</td><td>${\n            players[i].score\n        }</td>`;\n    }\n    if (players.length < 5) {\n        let cnt_players = players.length;\n        for (let i = cnt_players; i < 5; ++i){\n            rows[i + 1].innerHTML = `<td></td><td></td><td></td>`;\n        }\n    }\n    for(let i = data.length; i < 5; ++i){\n        rows[i+1].innerHTML = '<td>:</td><td>-</td><td>-</td>'\n    }\n}\n\nfunction setLeaderboardHidden(hidden) {\n    if (hidden) {\n        leaderboard.classList.add('hidden')\n    } else {\n        leaderboard.classList.remove('hidden')\n    }\n}\n\n\n//# sourceURL=webpack:///./client/leaderboard.js?");

/***/ }),

/***/ "./client/networking.js":
/*!******************************!*\
  !*** ./client/networking.js ***!
  \******************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

"use strict";
eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export */ __webpack_require__.d(__webpack_exports__, {\n/* harmony export */   \"socket\": () => (/* binding */ socket),\n/* harmony export */   \"connect\": () => (/* binding */ connect),\n/* harmony export */   \"play\": () => (/* binding */ play),\n/* harmony export */   \"updateDirection\": () => (/* binding */ updateDirection),\n/* harmony export */   \"createBullet\": () => (/* binding */ createBullet),\n/* harmony export */   \"addDamage\": () => (/* binding */ addDamage),\n/* harmony export */   \"decDamage\": () => (/* binding */ decDamage),\n/* harmony export */   \"addReload\": () => (/* binding */ addReload),\n/* harmony export */   \"addHealth\": () => (/* binding */ addHealth),\n/* harmony export */   \"addRange\": () => (/* binding */ addRange),\n/* harmony export */   \"addRegen\": () => (/* binding */ addRegen),\n/* harmony export */   \"addSpeed\": () => (/* binding */ addSpeed)\n/* harmony export */ });\n/* harmony import */ var throttle_debounce__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! throttle-debounce */ \"../node_modules/throttle-debounce/esm/index.js\");\n/* harmony import */ var _state__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./state */ \"./client/state.js\");\n/* harmony import */ var _index__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./index */ \"./client/index.js\");\n\n\n\n\nconst Constants = __webpack_require__(/*! @constants/constants */ \"./shared/constants.js\");\n\nvar socket = io.connect(window.location.host, {reconnection: false})\n\nconst connectedPromise = new Promise((resolve, reject) => {\n    let connected = false;\n    const timeOut = 300;\n    socket.on('connect', () => {\n        connected = true;\n        resolve('Connected to server');\n    })\n    setTimeout(() => {\n        if (!connected) {\n            reject('Couldn\\'t connect to server.\\n' +\n                'Socket timeout');\n        }\n    }, timeOut)\n\n});\n\n\nconst connect = onGameOver => {\n    return new Promise((resolve, reject) => {\n        connectedPromise\n            .then((successMsg) => {\n                console.log(successMsg)\n                socket.on(Constants.MSG_TYPES.GAME_UPDATE, _state__WEBPACK_IMPORTED_MODULE_1__.processGameUpdate);\n                socket.on(Constants.MSG_TYPES.UPDATE_LABELS, _state__WEBPACK_IMPORTED_MODULE_1__.updateLabels)\n                socket.on(Constants.MSG_TYPES.GAME_OVER, onGameOver)\n                socket.on('disconnect', onDisconnected);\n                resolve();\n            })\n            .catch((errorMsg) => {\n                console.error(errorMsg)\n                reject();\n            })\n    })\n}\n\n\nfunction onDisconnected() {\n    console.log('Disconnected from server');\n    document.getElementById('disconnect-modal').classList.remove('hidden');\n    document.getElementById('reconnect-button').onclick = () => {\n        window.location.reload();\n    }\n}\n\n\nconst play = player_data => {\n    socket.emit(Constants.MSG_TYPES.JOIN_GAME, player_data);\n\n    const canvas_size = _index__WEBPACK_IMPORTED_MODULE_2__.canvasWidth > _index__WEBPACK_IMPORTED_MODULE_2__.canvasHeight ? _index__WEBPACK_IMPORTED_MODULE_2__.canvasWidth : _index__WEBPACK_IMPORTED_MODULE_2__.canvasHeight\n    socket.emit(Constants.MSG_TYPES.CANVAS_GET, canvas_size);\n}\n\n\nconst updateDirection = (0,throttle_debounce__WEBPACK_IMPORTED_MODULE_0__.throttle)(100, (update_data) => {\n    socket.emit(Constants.MSG_TYPES.UPDATE_INPUT, update_data);\n})\n\n\nconst createBullet = (0,throttle_debounce__WEBPACK_IMPORTED_MODULE_0__.throttle)(100, (dir) => {\n    socket.emit(Constants.MSG_TYPES.NEW_BULLET, dir);\n})\n\n\n// Update players\nconst addDamage = (damageData) => {\n    socket.emit(Constants.MSG_TYPES.DAMAGE_ADD, damageData);\n}\n\nconst decDamage = (damageData) => {\n    socket.emit(Constants.MSG_TYPES.DAMAGE_DEC, damageData);\n}\n\nconst addReload = (reloadData) => {\n    socket.emit(Constants.MSG_TYPES.RELOAD_ADD, reloadData);\n}\n\nconst addHealth = (healthData) => {\n    socket.emit(Constants.MSG_TYPES.HEALTH_ADD, healthData);\n}\n\nconst addRange = (rangeData) => {\n    socket.emit(Constants.MSG_TYPES.RANGE_ADD, rangeData);\n}\n\nconst addRegen = (regenData) => {\n    socket.emit(Constants.MSG_TYPES.REGEN_ADD, regenData);\n}\n\nconst addSpeed = (speedData) => {\n    socket.emit(Constants.MSG_TYPES.SPEED_ADD, speedData);\n}\n\n//# sourceURL=webpack:///./client/networking.js?");

/***/ }),

/***/ "./client/render.js":
/*!**************************!*\
  !*** ./client/render.js ***!
  \**************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

"use strict";
eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export */ __webpack_require__.d(__webpack_exports__, {\n/* harmony export */   \"startRendering\": () => (/* binding */ startRendering),\n/* harmony export */   \"stopRendering\": () => (/* binding */ stopRendering)\n/* harmony export */ });\n/* harmony import */ var _state__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./state */ \"./client/state.js\");\n/* harmony import */ var _constants_constants__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @constants/constants */ \"./shared/constants.js\");\n/* harmony import */ var _constants_constants__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_constants_constants__WEBPACK_IMPORTED_MODULE_1__);\n/* harmony import */ var _index__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./index */ \"./client/index.js\");\n\n\n\n\nconst canvas = document.querySelector('canvas');\nlet c = canvas.getContext('2d');\n\ncanvas.width = window.innerWidth;\ncanvas.height = window.innerHeight;\n\nlet zoom = 1;\n\n\nfunction render() {\n    if (!(0,_state__WEBPACK_IMPORTED_MODULE_0__.getCurrentState)()){\n        return;\n    }\n    const {me, others, bullets, food} = (0,_state__WEBPACK_IMPORTED_MODULE_0__.getCurrentState)();\n\n    c.clearRect(0, 0, canvas.width, canvas.height);\n    c.save();\n    c.translate(canvas.width/2, canvas.height/2);\n    let newZoom = 30  / me.r;\n    zoom = lerp(zoom, newZoom, 0.1);\n\n    c.scale(zoom + 0.5, zoom + 0.5);\n    c.translate(-me.position.x, -me.position.y);\n\n    // draw boundaries\n    c.fillStyle = 'black';\n    c.lineWidth = 1;\n    c.strokeRect(-(_constants_constants__WEBPACK_IMPORTED_MODULE_1___default().MAP_SIZE), -(_constants_constants__WEBPACK_IMPORTED_MODULE_1___default().MAP_SIZE), (_constants_constants__WEBPACK_IMPORTED_MODULE_1___default().MAP_SIZE)*2, (_constants_constants__WEBPACK_IMPORTED_MODULE_1___default().MAP_SIZE)*2);\n\n    food.forEach(foody => renderFood(foody));\n    bullets.forEach(bullet => renderBullet(bullet));\n\n    others.forEach(player => renderPlayer(player));\n    renderPlayer(me);\n\n    c.restore();\n\n    // draw score_to_next lvl\n    c.beginPath();\n    c.fillStyle = 'yellow';\n    c.fillRect(300, 100,  800, 10);\n    c.fillStyle = 'blue';\n    c.fillRect(300, 100,800 *  (1 - ((Math.pow(me.lvl, 2) - me.score_to_next_lvl) /\n        Math.pow(me.lvl, 2))), 10);\n\n    // Draw score\n    c.beginPath();\n    c.fillStyle = \"black\";\n    c.textAlign = \"center\";\n    c.font = '30px serif';\n    let score_msg = \"Score: \" + me.score.toString();\n    c.fillText(score_msg, _index__WEBPACK_IMPORTED_MODULE_2__.canvasWidth * 0.08, _index__WEBPACK_IMPORTED_MODULE_2__.canvasHeight * 0.08);\n    c.fill();\n\n    // draw level\n    c.beginPath();\n    c.fillStyle = \"black\";\n    c.textAlign = \"center\";\n    c.font = '30px serif';\n    let level_msg = \"Level: \" + me.lvl.toString();\n    c.fillText(level_msg, _index__WEBPACK_IMPORTED_MODULE_2__.canvasWidth * 0.08, _index__WEBPACK_IMPORTED_MODULE_2__.canvasHeight * 0.15);\n\n    // draw free point to update\n    c.beginPath();\n    c.fillStyle = \"black\";\n    c.textAlign = \"center\";\n    c.font = '30px serif';\n    let points_msg = \"Free points: \" + me.update_points;\n    c.fillText(points_msg, _index__WEBPACK_IMPORTED_MODULE_2__.canvasWidth * 0.08, _index__WEBPACK_IMPORTED_MODULE_2__.canvasHeight * 0.22);\n}\n\n\nlet strokeColor = getRandomColor();\nfunction renderPlayer(player) {\n    // draw player\n    c.beginPath();\n    c.arc(player.position.x, player.position.y, player.r, 0, Math.PI * 2, false);\n    c.fillStyle = player.color;\n    c.fill();\n    if (player.r < 30){\n        c.lineWidth = 4;\n    } else{\n        c.lineWidth = player.r / 10;\n    }\n    c.strokeStyle = strokeColor;\n    c.stroke();\n\n    // draw health bar\n    c.beginPath();\n    c.fillStyle = 'white';\n    c.fillRect(player.position.x - player.r * 0.8, player.position.y - 2, player.r * 2 * 0.8, 4);\n    c.fillStyle = 'red';\n    c.fillRect(player.position.x - player.r * 0.8, player.position.y - 2,player.r * 2 * 0.8 *\n        ((1 - ((player.hp_max - player.hp) / player.hp_max))), 4);\n    c.fillStyle = player.color;\n    c.textAlign = 'center';\n\n    // draw nickname\n    c.beginPath();\n    let font_size = Math.floor((player.r / 2.7)).toString() + 'px';\n    let font = \" Comic Sans MS\";\n\n    c.font = player.r > 35 ? font_size + font : \"15px Comic Sans MS\";\n    let text_offset = player.r < 30 ? 5 : 10;\n\n    c.strokeStyle = strokeColor;\n    c.lineWidth = 4;\n    c.strokeText(player.nickname, player.position.x, player.position.y - text_offset);\n    c.fillStyle = 'white';\n    c.fillText(player.nickname, player.position.x, player.position.y - text_offset);\n}\n\n\nfunction renderBullet(bullet) {\n    c.beginPath();\n    c.arc(bullet.position.x, bullet.position.y, bullet.r, 0, Math.PI * 2, false);\n    c.fillStyle = 'red';\n    c.fill();\n}\n\n\nfunction renderFood(food){\n    c.beginPath();\n    c.arc(food.position.x, food.position.y, food.r, 0, Math.PI * 2, false);\n    c.fillStyle = food.color;\n    c.fill();\n}\n\n\nlet renderInterval = null;\nfunction startRendering() {\n    clearInterval(renderInterval)\n    renderInterval = setInterval(render, 1000/60);\n}\n\n\nfunction stopRendering() {\n    clearInterval(renderInterval);\n}\n\n\n// interpolation function to smoothly difference\nfunction lerp(start, end, t){\n    return start * (1-t) + end * t;\n}\n\n\nfunction getRandomColor() {\n    let letters = '0123456789ABCDEF';\n    let color = \"#\";\n    for (let i = 0; i < 6; ++i) {\n        color += letters[Math.floor(Math.random() * 16)];\n    }\n    return color;\n}\n\n\n//# sourceURL=webpack:///./client/render.js?");

/***/ }),

/***/ "./client/state.js":
/*!*************************!*\
  !*** ./client/state.js ***!
  \*************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

"use strict";
eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export */ __webpack_require__.d(__webpack_exports__, {\n/* harmony export */   \"processGameUpdate\": () => (/* binding */ processGameUpdate),\n/* harmony export */   \"updateLabels\": () => (/* binding */ updateLabels),\n/* harmony export */   \"getCurrentState\": () => (/* binding */ getCurrentState)\n/* harmony export */ });\n/* harmony import */ var _leaderboard__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./leaderboard */ \"./client/leaderboard.js\");\n/* harmony import */ var _upgrade__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./upgrade */ \"./client/upgrade.js\");\n\n\n\nconst upgradeMenu = document.getElementById('upgrade-menu');\nconst RENDER_DELAY = 100;\n\nconst gameUpdates = [];\nlet lastGameUpdate = null;\nlet got_update = false;\n\n\nfunction processGameUpdate(update) {\n    got_update = true;\n    lastGameUpdate = update;\n    (0,_leaderboard__WEBPACK_IMPORTED_MODULE_0__.updateLeaderboard)(update.leaderboard)\n    if (update.me.update_points < 1) {\n        upgradeMenu.classList.add('disabled');\n    }\n    else {\n        upgradeMenu.classList.remove('disabled');\n    }\n}\n\n\nfunction updateLabels(labels_data){\n    (0,_upgrade__WEBPACK_IMPORTED_MODULE_1__.update_lvl_labels)(labels_data);\n}\n\n\nfunction getCurrentState() {\n    if (!got_update) {\n        return false\n    }\n    return lastGameUpdate;\n}\n\n\n\n//# sourceURL=webpack:///./client/state.js?");

/***/ }),

/***/ "./client/upgrade.js":
/*!***************************!*\
  !*** ./client/upgrade.js ***!
  \***************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

"use strict";
eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export */ __webpack_require__.d(__webpack_exports__, {\n/* harmony export */   \"update_lvl_labels\": () => (/* binding */ update_lvl_labels)\n/* harmony export */ });\nconst upgrade_menu = document.getElementById('upgrade-menu');\n\nconst damageUpLvl = document.getElementById('dmgUp-lbl');\nconst damageDownLvl = document.getElementById('dmgDec-lbl');\nconst rangeLvl = document.getElementById('range-lbl');\nconst reloadLvl = document.getElementById('reload-lbl');\nconst speedLvl = document.getElementById('speed-lbl');\nconst healthLvl = document.getElementById('health-lbl');\nconst regenLvl = document.getElementById('regen-lbl');\n\n\nfunction update_lvl_labels(data){\n    damageUpLvl.innerHTML = data.damageUpLvl;\n    damageDownLvl.innerHTML = data.damageDecLvl;\n    rangeLvl.innerHTML = data.rangeLvl;\n    regenLvl.innerHTML = data.regenLvl;\n    reloadLvl.innerHTML = data.reloadLvl;\n    speedLvl.innerHTML = data.speedLvl;\n    healthLvl.innerHTML = data.healthLvl;\n}\n\n\n\n\n\n\n//# sourceURL=webpack:///./client/upgrade.js?");

/***/ }),

/***/ "./shared/constants.js":
/*!*****************************!*\
  !*** ./shared/constants.js ***!
  \*****************************/
/***/ ((module) => {

eval("module.exports = Object.freeze({\n    PLAYER_MAX_HP: 100,\n    PLAYER_RADIUS: 12,\n    PLAYERS_SPEED: 1,\n    PLAYER_MAX_REGEN_TIME: 5000,\n    PLAYER_MIN_REGEN_TIME: 1000,\n\n\n    BULLET_MIN_RANGE_SHOOT: 300,\n\n    BULLET_RADIUS: 10,\n    BULLET_SPEED: 10,\n    BULLET_DAMAGE: 5,\n    SCORE_BULLET_HIT: 20,\n\n    SCORE_FOR_FOOD: 1,\n\n    FOOD_RADIUS: 10,\n\n    MAP_SIZE: 1000,\n    MSG_TYPES: {\n\n        DAMAGE_ADD: 'damage_add',\n        DAMAGE_DEC: 'damage_dec',\n        HEALTH_ADD: 'health_add',\n        SPEED_ADD: 'speed_add',\n        RANGE_ADD: 'range_add',\n        RELOAD_ADD: 'reload_add',\n        REGEN_ADD: 'regen_add',\n        UPDATE_LABELS: 'labels_update',\n\n        CANVAS_GET: 'canvas_get',\n        UPDATE_INPUT: 'update_input',\n        NEW_BULLET: 'new_bullet',\n        JOIN_GAME: 'join_game',\n        GAME_UPDATE: 'game_update',\n        GAME_OVER: 'dead'\n    }\n});\n\n//# sourceURL=webpack:///./shared/constants.js?");

/***/ })

/******/ 	});
/************************************************************************/
/******/ 	// The module cache
/******/ 	var __webpack_module_cache__ = {};
/******/ 	
/******/ 	// The require function
/******/ 	function __webpack_require__(moduleId) {
/******/ 		// Check if module is in cache
/******/ 		var cachedModule = __webpack_module_cache__[moduleId];
/******/ 		if (cachedModule !== undefined) {
/******/ 			return cachedModule.exports;
/******/ 		}
/******/ 		// Create a new module (and put it into the cache)
/******/ 		var module = __webpack_module_cache__[moduleId] = {
/******/ 			// no module.id needed
/******/ 			// no module.loaded needed
/******/ 			exports: {}
/******/ 		};
/******/ 	
/******/ 		// Execute the module function
/******/ 		__webpack_modules__[moduleId](module, module.exports, __webpack_require__);
/******/ 	
/******/ 		// Return the exports of the module
/******/ 		return module.exports;
/******/ 	}
/******/ 	
/******/ 	// expose the modules object (__webpack_modules__)
/******/ 	__webpack_require__.m = __webpack_modules__;
/******/ 	
/************************************************************************/
/******/ 	/* webpack/runtime/chunk loaded */
/******/ 	(() => {
/******/ 		var deferred = [];
/******/ 		__webpack_require__.O = (result, chunkIds, fn, priority) => {
/******/ 			if(chunkIds) {
/******/ 				priority = priority || 0;
/******/ 				for(var i = deferred.length; i > 0 && deferred[i - 1][2] > priority; i--) deferred[i] = deferred[i - 1];
/******/ 				deferred[i] = [chunkIds, fn, priority];
/******/ 				return;
/******/ 			}
/******/ 			var notFulfilled = Infinity;
/******/ 			for (var i = 0; i < deferred.length; i++) {
/******/ 				var [chunkIds, fn, priority] = deferred[i];
/******/ 				var fulfilled = true;
/******/ 				for (var j = 0; j < chunkIds.length; j++) {
/******/ 					if ((priority & 1 === 0 || notFulfilled >= priority) && Object.keys(__webpack_require__.O).every((key) => (__webpack_require__.O[key](chunkIds[j])))) {
/******/ 						chunkIds.splice(j--, 1);
/******/ 					} else {
/******/ 						fulfilled = false;
/******/ 						if(priority < notFulfilled) notFulfilled = priority;
/******/ 					}
/******/ 				}
/******/ 				if(fulfilled) {
/******/ 					deferred.splice(i--, 1)
/******/ 					result = fn();
/******/ 				}
/******/ 			}
/******/ 			return result;
/******/ 		};
/******/ 	})();
/******/ 	
/******/ 	/* webpack/runtime/compat get default export */
/******/ 	(() => {
/******/ 		// getDefaultExport function for compatibility with non-harmony modules
/******/ 		__webpack_require__.n = (module) => {
/******/ 			var getter = module && module.__esModule ?
/******/ 				() => (module['default']) :
/******/ 				() => (module);
/******/ 			__webpack_require__.d(getter, { a: getter });
/******/ 			return getter;
/******/ 		};
/******/ 	})();
/******/ 	
/******/ 	/* webpack/runtime/define property getters */
/******/ 	(() => {
/******/ 		// define getter functions for harmony exports
/******/ 		__webpack_require__.d = (exports, definition) => {
/******/ 			for(var key in definition) {
/******/ 				if(__webpack_require__.o(definition, key) && !__webpack_require__.o(exports, key)) {
/******/ 					Object.defineProperty(exports, key, { enumerable: true, get: definition[key] });
/******/ 				}
/******/ 			}
/******/ 		};
/******/ 	})();
/******/ 	
/******/ 	/* webpack/runtime/global */
/******/ 	(() => {
/******/ 		__webpack_require__.g = (function() {
/******/ 			if (typeof globalThis === 'object') return globalThis;
/******/ 			try {
/******/ 				return this || new Function('return this')();
/******/ 			} catch (e) {
/******/ 				if (typeof window === 'object') return window;
/******/ 			}
/******/ 		})();
/******/ 	})();
/******/ 	
/******/ 	/* webpack/runtime/hasOwnProperty shorthand */
/******/ 	(() => {
/******/ 		__webpack_require__.o = (obj, prop) => (Object.prototype.hasOwnProperty.call(obj, prop))
/******/ 	})();
/******/ 	
/******/ 	/* webpack/runtime/make namespace object */
/******/ 	(() => {
/******/ 		// define __esModule on exports
/******/ 		__webpack_require__.r = (exports) => {
/******/ 			if(typeof Symbol !== 'undefined' && Symbol.toStringTag) {
/******/ 				Object.defineProperty(exports, Symbol.toStringTag, { value: 'Module' });
/******/ 			}
/******/ 			Object.defineProperty(exports, '__esModule', { value: true });
/******/ 		};
/******/ 	})();
/******/ 	
/******/ 	/* webpack/runtime/jsonp chunk loading */
/******/ 	(() => {
/******/ 		// no baseURI
/******/ 		
/******/ 		// object to store loaded and loading chunks
/******/ 		// undefined = chunk not loaded, null = chunk preloaded/prefetched
/******/ 		// [resolve, reject, Promise] = chunk loading, 0 = chunk loaded
/******/ 		var installedChunks = {
/******/ 			"game": 0
/******/ 		};
/******/ 		
/******/ 		// no chunk on demand loading
/******/ 		
/******/ 		// no prefetching
/******/ 		
/******/ 		// no preloaded
/******/ 		
/******/ 		// no HMR
/******/ 		
/******/ 		// no HMR manifest
/******/ 		
/******/ 		__webpack_require__.O.j = (chunkId) => (installedChunks[chunkId] === 0);
/******/ 		
/******/ 		// install a JSONP callback for chunk loading
/******/ 		var webpackJsonpCallback = (parentChunkLoadingFunction, data) => {
/******/ 			var [chunkIds, moreModules, runtime] = data;
/******/ 			// add "moreModules" to the modules object,
/******/ 			// then flag all "chunkIds" as loaded and fire callback
/******/ 			var moduleId, chunkId, i = 0;
/******/ 			for(moduleId in moreModules) {
/******/ 				if(__webpack_require__.o(moreModules, moduleId)) {
/******/ 					__webpack_require__.m[moduleId] = moreModules[moduleId];
/******/ 				}
/******/ 			}
/******/ 			if(runtime) var result = runtime(__webpack_require__);
/******/ 			if(parentChunkLoadingFunction) parentChunkLoadingFunction(data);
/******/ 			for(;i < chunkIds.length; i++) {
/******/ 				chunkId = chunkIds[i];
/******/ 				if(__webpack_require__.o(installedChunks, chunkId) && installedChunks[chunkId]) {
/******/ 					installedChunks[chunkId][0]();
/******/ 				}
/******/ 				installedChunks[chunkIds[i]] = 0;
/******/ 			}
/******/ 			return __webpack_require__.O(result);
/******/ 		}
/******/ 		
/******/ 		var chunkLoadingGlobal = self["webpackChunk"] = self["webpackChunk"] || [];
/******/ 		chunkLoadingGlobal.forEach(webpackJsonpCallback.bind(null, 0));
/******/ 		chunkLoadingGlobal.push = webpackJsonpCallback.bind(null, chunkLoadingGlobal.push.bind(chunkLoadingGlobal));
/******/ 	})();
/******/ 	
/************************************************************************/
/******/ 	
/******/ 	// startup
/******/ 	// Load entry module and return exports
/******/ 	// This entry module depends on other loaded chunks and execution need to be delayed
/******/ 	var __webpack_exports__ = __webpack_require__.O(undefined, ["vendors-node_modules_lodash_escape_js-node_modules_throttle-debounce_esm_index_js"], () => (__webpack_require__("./client/index.js")))
/******/ 	__webpack_exports__ = __webpack_require__.O(__webpack_exports__);
/******/ 	
/******/ })()
;