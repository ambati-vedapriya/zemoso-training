import { makeStyles, } from "@mui/styles"
import { Box } from '@mui/material';
import { CustomTable } from "../components/CustomTable";
import {ThemeProvider} from'@mui/material'
import { Typography } from '@mui/material';
import InfoOutlinedIcon from '@mui/icons-material/InfoOutlined';
import { createTheme } from "@mui/material/styles";

const useStyles = makeStyles((theme) => ({
  root: {
    backgroundColor: 'black', // outer box background color
   padding:'50px',
    width: '700px', // custom width of the outer box
    height: '400px', 
    marginLeft:'100px',
  },
  innerBox: {
    backgroundColor: 'black', // inner box background color
    
  
    width: '700px', // custom width of the inner box
    height: '200px', // custom height of the inner box
  },
}));
const theme = createTheme({
  palette: {
    text: {
      primary: 'white',
    },
    
  },
  typography:{
    h4:{
      color:"white",
     
    },
},
});

export function StateAssing() {
  const classes = useStyles();

  return (
    <ThemeProvider theme={theme}>
    <Box className={classes.root}>
    <Typography variant='h4' mb={2}>Yours Contracts
      <InfoOutlinedIcon style={{marginBottom:'-5px',fontSize:'30px',marginLeft:'5px'}}></InfoOutlinedIcon></Typography>
      <Box className={classes.innerBox}>
        <CustomTable/>
      </Box>
    </Box>
    </ThemeProvider>
  );
}
