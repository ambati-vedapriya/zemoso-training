import React, { ReactNode, ChangeEvent } from "react";
import { InputAdornment, TextField } from "@mui/material";

export interface ITextFieldProps {
  variant: "outlined" | "standard" | "filled";
  placeholder: string;
  type: "text" | "email" | "password";
  sx?: object;
  textFieldIcon: ReactNode;
  value?: string;
  onChange?: (event: ChangeEvent<HTMLInputElement>) => void;
}
const Input = (props: ITextFieldProps) => {
  return (
    <TextField
      variant={props.variant}
      placeholder={props.placeholder}
      type={props.type}
      sx={props.sx}
      value={props.value}
      onChange={props.onChange}
      InputProps={{
        endAdornment: (
          <InputAdornment position="end">{props.textFieldIcon}</InputAdornment>
        ),
      }}
    />
  );
};

export default Input;
