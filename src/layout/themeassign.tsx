import { createTheme, colors, ThemeProvider } from '@mui/material'
import MuiText from '../components/MuiText';
import MuiButton from '../components/MuiButton';
import { Box } from '@mui/system';
import ReceiptLongIcon from '@mui/icons-material/ReceiptLong';

const theme = createTheme({
    palette: {
      secondary: {
        main: colors.grey[900]
      },
      primary: {
        main: colors.pink[300]
      }
    }
  
  })

  export function ThemeAssing(){
    return(
        <div>
      <ThemeProvider theme={theme}>
        <Box
          sx={{
            height: "300px",
            width: "300px",
            backgroundColor: "secondary.main",
            marginLeft: "40%",
            marginTop: "20px",
            borderRadius: "5px"
          }
          }>
          <MuiButton></MuiButton>
          <ReceiptLongIcon color='primary' 
          style={{ fontSize: "60px", 
          marginTop: "120px", 
          marginLeft: "25px", 
          transform: "rotate(180deg)", 
          backgroundColor: "#37474f", 
          borderRadius: "5px" }}>
          </ReceiptLongIcon>
          <MuiText></MuiText>
        </Box>

      </ThemeProvider>
    </div>
    )
  }