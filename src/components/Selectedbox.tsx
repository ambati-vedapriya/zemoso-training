import React, { useState } from "react";
import {
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  Checkbox,
} from "@mui/material";

type Data = {
  id: number;
  name: string;
  age: number;
};

const initialData: Data[] = [
  { id: 1, name: "John Doe", age: 25 },
  { id: 2, name: "Jane Doe", age: 30 },
  { id: 3, name: "Bob Smith", age: 35 },
];

export const StateAssing = () => {
  const [selected, setSelected] = useState<number[]>([]);

  const handleSelect = (id: number) => {
    if (selected.includes(id)) {
      setSelected(selected.filter((s) => s !== id));
    } else {
      setSelected([...selected, id]);
    }
  };

  return (
    <TableContainer>
      <Table>
        <TableHead>
          <TableRow>
            <TableCell />
            <TableCell>Name</TableCell>
            <TableCell>Age</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {initialData.map((data) => (
            <TableRow key={data.id}>
              <TableCell>
                <Checkbox
                  checked={selected.includes(data.id)}
                  onChange={() => handleSelect(data.id)}
                />
              </TableCell>
              <TableCell>{data.name}</TableCell>
              <TableCell>{data.age}</TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
  );
}




