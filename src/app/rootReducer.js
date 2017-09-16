import {
  combineReducers
} from 'redux'
import {
  IntlReducer as Intl
} from 'react-redux-multilingual'
import {
  commonReducer
} from './modules/common/commonReducer'
import {
  matchupReducer
} from './modules/common/matchupReducer'

const rootReducer = combineReducers({
  common: commonReducer,
  Intl,
  matchupReducer
})

export default function root(state = {}, action) {
  return rootReducer(state, action)
}
