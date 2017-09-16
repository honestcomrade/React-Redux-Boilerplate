"use strict"

export function matchupReducer(state={matchup:[]}, action) {
  switch(action.type){
    case "GET_MATCHUP":
      return {...state,
        matchup:action.payload,
      }
    default:
      return{ ...state}
    }
}
