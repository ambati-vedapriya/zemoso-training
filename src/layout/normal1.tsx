import React, { useState } from 'react';
import { Table, TableBody, TableCell, TableHead, TableRow, Checkbox } from '@mui/material';

interface TableData {
  id: number;
  name: string;
  selected: boolean;
}

const initialData: TableData[] = [
  { id: 1, name: 'Row 1', selected: false },
  { id: 2, name: 'Row 2', selected: false },
  { id: 3, name: 'Row 3', selected: false },
  { id: 4, name: 'Row 4', selected: false },
];

export const CustomTable: React.FC = () => {
  const [tableData, setTableData] = useState<TableData[]>(initialData);

  const handleCheckboxChange = (id: number) => {
    const updatedTableData = tableData.map((row) => {
      if (row.id === id) {
        return { ...row, selected: !row.selected };
      }
      return row;
    });
    setTableData(updatedTableData);
  };

  return (
    <Table>
      <TableHead>
        <TableRow>
          <TableCell>Select</TableCell>
          <TableCell>Name</TableCell>
        </TableRow>
      </TableHead>
      <TableBody>
        {tableData.map((row) => (
          <TableRow key={row.id} style={{ backgroundColor: row.selected ? '#007bff' : 'transparent' }}>
            <TableCell>
              <Checkbox
                color="primary"
                checked={row.selected}
                onChange={() => handleCheckboxChange(row.id)}
              />
            </TableCell>
            <TableCell>{row.name}</TableCell>
          </TableRow>
        ))}
      </TableBody>
    </Table>
  );
};


