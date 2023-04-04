import React, { useState } from "react";
import { Checkbox, Table, TableBody, TableCell, TableContainer, TableHead, TableRow, Paper ,} from "@mui/material";
import {makeStyles,createStyles} from "@mui/styles"
import { white } from "material-ui/styles/colors";
import { Stack } from "@mui/material";
import { Box } from "@mui/material";
import { width } from "@mui/system";

interface Row {
  id: number;
  Name: string;
  Type:string;
  Peerpayment:string;
  TermLength:string;
}

const rows: Row[] = [
  { id: 1, Name: "Contract1", Type:"Monthly", Peerpayment:"$12,000.25" ,TermLength:"12 months 12% fee"},
  { id: 2, Name: "Contract2", Type:"Monthly", Peerpayment:"$12,000.25" ,TermLength:"12 months 12% fee"},
  { id: 3, Name: "Contract3",Type:"Monthly", Peerpayment:"$12,000.25" ,TermLength:"12 months 12% fee" },
  { id: 4, Name: "Contract4",Type:"Monthly", Peerpayment:"$12,000.25" ,TermLength:"12 months 12% fee" },
  { id: 5, Name: "Contract5",Type:"Monthly", Peerpayment:"$12,000.25" ,TermLength:"12 months 12% fee" },
  { id: 6, Name: "Contract6",Type:"Monthly", Peerpayment:"$12,000.25" ,TermLength:"12 months 12% fee" },

];

const useStyles:any = makeStyles(() =>
  createStyles({
    table: {
      backgroundColor: '#263238',
     
      color: 'white', 
      
    },
    tableBody: {
      backgroundColor: '#263238',
       
    },
    tableCell: {
      padding: '8px 16px', 
    },
  })
);


export const Custom = () => {
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
    return isRowSelected(id) ? "#b39ddb" : "#263238";
  };

    const classes = useStyles();
  return (
    <Box>

    <Stack>
    <TableContainer component={Paper}>
      <Table className={classes.table} size="small">
        <TableHead>
          <TableRow>
            <TableCell className={classes.tableCell}>
              <Checkbox 
                checked={allChecked}
                onChange={handleSelectAll}
              />
            </TableCell>
            <TableCell className={classes.tableCell}>Name</TableCell>
            <TableCell className={classes.tableCell}>Type</TableCell>
            <TableCell className={classes.tableCell}>Peer payment</TableCell>
            <TableCell className={classes.tableCell}>Term Length</TableCell>
            
          </TableRow>
        </TableHead>
        <TableBody className={classes.tableBody}>
          {rows.map((row) => (
            <TableRow
              key={row.id}
              style={{ backgroundColor: rowColor(row.id) }}
            >
              <TableCell className={classes.tableCell}>
                <Checkbox style={{ color: "#7b1fa2" }}
                  checked={isRowSelected(row.id)}
                  onChange={(event) => handleSelectRow(event, row.id)}
                />
              </TableCell>
              <TableCell className={classes.tableCell}>{row.Name}</TableCell>
              <TableCell className={classes.tableCell}>{row.Type}</TableCell>
              <TableCell className={classes.tableCell}>{row.Peerpayment}</TableCell>
              <TableCell className={classes.tableCell}>{row.TermLength}</TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
    </Stack>
  </Box>
  );
}
