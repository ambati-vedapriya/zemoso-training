import { Button, ButtonProps } from "@mui/material";
interface ButtonProp extends ButtonProps {
  text: String;
}

const MuiButton = (props: ButtonProp) => {
  return (
    <Button variant={props.variant} {...props}>
      {props.text}
    </Button>
  );
};
export default MuiButton;
