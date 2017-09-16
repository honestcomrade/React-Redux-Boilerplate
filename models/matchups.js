"use strict"

const mongoose = require('mongoose');

const matchupsSchema = mongoose.Schema({
  home: Boolean,
  score: Number,
  team:{
    record:{
      awayPercentage: Number,
      divisionStanding: Number,
      overallStanding: Number,
      divisionLosses: Number,
      homePercentage: Number,
      awayTies: Number,
      divisionWins: Number,
      streakType: Number,
      overallTies: Number,
      homeTies: Number,
      homeWins: Number,
      divisionTies: Number,
      overallPercentage: Number,
      overallWins: Number,
      overallLosses: Number,
      streakLength: Number,
      pointsAgainst: Number,
      awayWins: Number,
      divisionPercentage: Number,
      homeLosses: Number,
      pointsFor: Number,
      awayLosses: Number
    },
    waiverRank: Number,
    division:{
      divisionName: String,
      divisionId: Number,
      size: Number
    },
    teamAbbrev: String,
    teamNickname: String,
    logoUrl: String,
    teamLocation: String,
    teamId: Number
  },
  teamId: Number
})

const Matchups = mongoose.model('Matchups', matchupsSchema)

module.exports = Matchups;
