import React, { Component } from 'react'
import { connect } from 'react-redux'
import { bindActionCreators } from 'redux'
import { Link } from 'react-router'
import banner from '../../../resources/assets/images/banner.jpg'
import './Home.scss'
import * as matchupActions from '../../common/actions/matchupActions'


class Home extends Component {
  componentDidMount() {
    console.log("PROP:", this.props)
    // if(this.props.matchup.length == 0) {
      this.props.actions.getMatchup();
    // }
  }

  constructor(props) {
    super(props)
    this.state = {
    }
  }

  render() {
    return (
      <div className="home">
        <div className="home__content">
          <a href="#" className="home__logo-link">
            <img src={banner} alt="Football" className="header-banner" />
          </a>
          <h4 className="home__heading">Offensive Fowlers</h4>
          <nav className="home__nav">
            <ul className="home__nav-list">
              <li className="home__nav-list-item">
                <Link to="/team" className="home__nav-list-link">TEAM</Link>
              </li>
              <li className="home__nav-list-item">
                <a href="http://games.espn.com/ffl/leagueoffice?leagueId=262704&seasonId=2017" target="_blank" rel="noopener noreferrer" className="home__nav-list-link">LEAGUE</a>
              </li>
              <li className="home__nav-list-item">
                <a href="https://github.com/honestcomrade" target="_blank" rel="noopener noreferrer" className="home__nav-list-link">SUPPORT</a>
              </li>
            </ul>
          </nav>
        </div>
      </div>
    )
  }
}

// Home.propTypes = {}

function mapStateToProps(state, ownProps) {
  return { matchup: state.matchup }
}

const mapDispatchToProps = dispatch => ({
  actions: bindActionCreators(matchupActions, dispatch)
})

export default connect(mapStateToProps, mapDispatchToProps)(Home)
