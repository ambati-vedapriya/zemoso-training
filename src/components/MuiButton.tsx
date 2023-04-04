import { Button } from '@mui/material'
import React from 'react'

const MuiButton = () => {
  return (
    <div>
      <Button variant="contained" 
      size='small' 
      color='primary'
      style={{float:'right',
      marginTop:'15px',
      marginRight:'10px',
      fontFamily:'Arial',
    }}
      >Due in 30 day(s)</Button>
    </div>
  )
}

export default MuiButton