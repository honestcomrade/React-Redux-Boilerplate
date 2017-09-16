"use strict"

import axios from 'axios';

export function getMatchup() {
  return function(dispatch) {
    axios.get('../../../../../../db/team.json')
    .then(function(response) {
      dispatch({type: "GET_MATCH", payload:response.data})
    })
    .catch(function(err) {
      dispatch({type: "GET_MATCH_REJECTED", msg:"ERROR WHEN GETTING MATCH"})
    })
  }
}
