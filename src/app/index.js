/* eslint "import/imports-first": 0 */
/* eslint no-undef: 0 */
/* eslint import/extensions: 0 */
/* eslint react/jsx-filename-extension:0 */
import React from 'react'
import ReactDOM from 'react-dom'
import 'babel-polyfill'
import logger from 'redux-logger';
import { Provider } from 'react-redux'
import { createStore, applyMiddleware, compose } from 'redux'
import createSagaMiddleware from 'redux-saga'
import { Router, browserHistory } from 'react-router'
import reducers from './rootReducer'
import routes from './routes'
import rootSaga from './rootSagas'
import translations from './translations'
import { IntlProvider } from 'react-redux-multilingual'
import thunk from 'redux-thunk'
// for bundling your styles
// import './bundle.scss'

const devtools = window.devToolsExtension || (() => noop => noop)
const initialState = window.INITIAL_STATE;

const sagaMiddleware = createSagaMiddleware()
const middlewares = [
  sagaMiddleware,
  logger,
  thunk
]

const enhancers = [
  applyMiddleware(...middlewares),
  devtools(),
]
const store = createStore(
  reducers,
  initialState,
  compose(...enhancers)
)

sagaMiddleware.run(rootSaga)

const locale = store.getState().Intl.locale

ReactDOM.render(
  <Provider store={store}>
    <IntlProvider translations={translations}>
      <Router history={browserHistory} routes={routes(locale)} />
    </IntlProvider>
  </Provider>
  , document.querySelector('.react-root'))
