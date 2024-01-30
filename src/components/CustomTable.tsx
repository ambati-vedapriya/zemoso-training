import React, { useState } from "react";
import { Checkbox, Table, TableBody, TableCell, TableContainer, TableHead, TableRow, Paper ,} from "@mui/material";
import {makeStyles,createStyles} from "@mui/styles"
import { Stack } from "@mui/material";
import { Box } from "@mui/material";


interface Row {
  id: number;
  Name: string;
  Type:string;
  Peerpayment:string;
  TermLength:string;
  per:string;
  payment:string;
}

const rows: Row[] = [
  { id: 1, Name: "Contract1", Type:"Monthly", Peerpayment:"$12,000.25" ,TermLength:"12 months",per:" 12% fee",payment:'$11,000'},
  { id: 2, Name: "Contract2", Type:"Monthly", Peerpayment:"$12,000.25" ,TermLength:"12 months 12% fee",per:" 12% fee",payment:'$11,000'},
  { id: 3, Name: "Contract3",Type:"Monthly", Peerpayment:"$12,000.25" ,TermLength:"12 months 12% fee",per:" 12% fee" ,payment:'$11,000'},
  { id: 4, Name: "Contract4",Type:"Monthly", Peerpayment:"$12,000.25" ,TermLength:"12 months 12% fee" , per:" 12% fee",payment:'$11,000'},
  { id: 5, Name: "Contract5",Type:"Monthly", Peerpayment:"$12,000.25" ,TermLength:"12 months 12% fee" ,per:" 12% fee",payment:'$11,000'},
  { id: 6, Name: "Contract6",Type:"Monthly", Peerpayment:"$12,000.25" ,TermLength:"12 months 12% fee" ,per:" 12% fee",payment:'$11,000'},

];

const useStyles:any = makeStyles(() =>
  createStyles({
    table: {
      backgroundColor: '#2e2c2c',
      borderRadius:'5px.'
  
    },
    tableBody: {
      backgroundColor: 'black',
      border:'none',
      
      
       
    },
    tableCell: {
      
      color: '#e0e0e0',
      borderBottom:'none',
     
     
    
    },
  })
);


export const CustomTable = () => {
  const [allChecked, setAllChecked] = useState(false);
  const [selectedRows, setSelectedRows] = useState<number[]>([]);
  
  const handleSelectAll = (event: React.ChangeEvent<HTMLInputElement>) => {
    if (event.target.checked) {
      setSelectedRows(rows.map((row) => row.id));
    } else {
      setSelectedRows([]);
    }
    setAllChecked(event.target.checked);
  };

  const handleSelectRow = (event: React.ChangeEvent<HTMLInputElement>, id: number) => {
    if (event.target.checked) {
      setSelectedRows([...selectedRows, id]);
    } else {
      setSelectedRows(selectedRows.filter((rowId) => rowId !== id));
    }
  };

  const isRowSelected = (id: number) => {
    return selectedRows.indexOf(id) !== -1;
  };

  const rowColor = (id: number) => {
    return isRowSelected(id) ? "rgba(179,136,255,0.2)" : "#2e2c2c";
  };

    const classes = useStyles();
  return (
    <Box>

    <Stack>
    <TableContainer component={Paper}>
      <Table className={classes.table} style={{borderBottom:"none"}} size="small">
        <TableHead>
          <TableRow>
            <TableCell className={classes.tableCell} style={{borderBottom:"none"}}>
              <Checkbox style={{ color: "#d500f9" }}
                checked={allChecked}
                onChange={handleSelectAll}
              />
            </TableCell>
            <TableCell className={classes.tableCell} style={{borderBottom:"none",color: '#9e9e9e',}}>Name</TableCell>
            <TableCell className={classes.tableCell} style={{borderBottom:"none",color: '#9e9e9e',}}>Type</TableCell>
            <TableCell className={classes.tableCell} style={{borderBottom:"none",color: '#9e9e9e',}}>Peer payment</TableCell>
            <TableCell className={classes.tableCell} style={{borderBottom:"none",color: '#9e9e9e',}}>Term Length</TableCell>
            <TableCell className={classes.tableCell} style={{borderBottom:"none",color: '#9e9e9e',}}>Payment</TableCell>
            
          </TableRow>
        </TableHead>
        <TableBody className={classes.tableBody}>
          {rows.map((row) => (
            <TableRow
              key={row.id}
              style={{ backgroundColor: rowColor(row.id) }}
            >
              <TableCell className={classes.tableCell} style={{borderBottom:"none"}}>
                <Checkbox style={{ color: "#d500f9" }}
                  checked={isRowSelected(row.id)}
                  onChange={(event) => handleSelectRow(event, row.id)}
                />
              </TableCell>
              <TableCell className={classes.tableCell} style={{borderBottom:"none",color: 'white',}}>{row.Name}</TableCell>
              <TableCell className={classes.tableCell} style={{borderBottom:"none",color: '#9e9e9e',}}>{row.Type}</TableCell>
              <TableCell className={classes.tableCell} style={{borderBottom:"none",color: '#9e9e9e',}}>{row.Peerpayment}<br></br>{row.per}</TableCell>
              <TableCell className={classes.tableCell} style={{borderBottom:"none",color: '#9e9e9e',}}>{row.TermLength}</TableCell>
              <TableCell className={classes.tableCell} style={{borderBottom:"none",color: '#9e9e9e',}}>{row.payment}</TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
    </Stack>
  </Box>
  );
}
//<IndeterminateCheckBoxOutlinedIcon style={{ color: "#d500f9" ,marginLeft:"6px", }} />