import React, { useState } from 'react';
import { TextField, Button } from '@material-ui/core';
import { makeStyles } from '@material-ui/core/styles';
import logo from '../../img/logo.png';
import axios from 'axios';
import SearchResult from '../SearchResults/SearchResult'
import HeaderSimple from './HeaderSimple';

const useStyles = makeStyles((theme) => ({
  container: {
    width: '100vw',
  },
  searchField: {
    width: '80vw',
    maxWidth: '700px',
    marginBottom: '25px',
  },
  logo: {
    width: '500px',
    height: '125px',
    marginBottom: '50px',
    // display: 'block',
  },
  buttonStyle: {
    marginLeft: '20px',
    width: '50px',
    height: '55px',
    textDecoration: 'none',
  },
  contents: {
    marginTop: '100px',
  },
}));

function LandingPage() {
  const styles = useStyles();
  const [query, changeQuery] = useState('');

  function handleQueryChange(event) {
    changeQuery(event.target.value);
  }

  async function makeSearch() {
    const { data } = await axios.get(`/search/${query}`);
    changeQuery('');
    console.log('Response: ' + data['message']);
  }
  return (
    <div className={styles.container}>
      <HeaderSimple />
      <div className={styles.contents}>
        <img src={logo} className={styles.logo} alt="Chefmate logo" />
        <br />
        <TextField
          id="outlined-search"
          label="Search"
          type="search"
          variant="outlined"
          className={styles.searchField}
          value={query}
          onChange={handleQueryChange}
        />
        <a href="/SearchResult">
        <Button
          variant="contained"
          className={styles.buttonStyle}
          // onClick={makeSearch}
        >GO
        </Button>
        </a>
        
      </div>
    </div>
  );
}

export default LandingPage;
