import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import { AppBar, Toolbar, Typography, Button, IconButton } from '@material-ui/core';
import { FaBars } from 'react-icons/fa';

const useStyles = makeStyles((theme) => ({
  barcolor: {
    background: 'rgb(230, 95, 85)',
  },
  root: {
    flexGrow: 1,
  },
  menuButton: {
    marginRight: theme.spacing(2),
  },
  title: {
    flexGrow: 1,
  },
  buttonStyle: {
    textDecoration: 'none',
    color: 'white',
  },
}));

export default function HeaderSimple() {
  const classes = useStyles();

  return (
    <div className={classes.root}>
      <AppBar position="static" className={classes.barcolor}>
        <Toolbar>
          <IconButton
            edge="start"
            className={classes.menuButton}
            color="inherit"
            aria-label="menu"
          >
            <FaBars />
          </IconButton>
          <Typography variant="h5" className={classes.title}>
            CHEFMATE
          </Typography>
          <a className={classes.buttonStyle} href="/logout">
            <Button color="inherit">Logout</Button>
          </a>
        </Toolbar>
      </AppBar>
    </div>
  );
}
