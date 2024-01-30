import React from 'react'
import { Box } from '@mui/system'
import { Typography } from '@mui/material'
import { createTheme, ThemeProvider } from '@mui/material/styles';
import InfoOutlinedIcon from '@mui/icons-material/InfoOutlined';

const theme = createTheme({
  typography:{
    body1:{
      color:"grey",
      mt:13,
    },
    h6:{
      color:"white",
    }
  }
})
const MuiText = () => {
  return (
    <Box >
      <ThemeProvider theme={theme}>
      <Typography variant='body1' ml={3} mt={2}>Due - May 03,2021
      <InfoOutlinedIcon style={{marginBottom:'-5px'}}></InfoOutlinedIcon></Typography>
      <Typography variant='h6' ml={3}>$14,204.55</Typography>
      </ThemeProvider>
    </Box>
  )
}

export default MuiText