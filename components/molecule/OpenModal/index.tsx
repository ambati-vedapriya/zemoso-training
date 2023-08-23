import styled from "@emotion/styled";
import { Typography } from "@mui/material";
import { MuiTypography } from "../../Atoms/Typography";
import MuiButton from "../../Atoms/Button";

const InnerBox = styled("div")(() => ({
  height: "300px",
  width: "600px",
  border: "1px solid black",
  alignItems: "center",
  padding: "20px",
  gap: "20px",
  position: "absolute",
  backgroundColor: "white",
}));

const EndBox = styled("div")(() => ({
  marginLeft: "350px",
  marginTop: "20px",
  display: "flex",
  gap: "20px",
  alignItems: "end",
}));

interface BoxProp {
  name: String;
  price: number;
}
interface prop {
  boxProps: BoxProp[];
  onCancel: () => void;
  onBuy: () => void;
}

const OpenModal = (props: prop) => {
  const getTotalPrice = () => {
    return props.boxProps.reduce((total, product) => total + product.price, 0);
  };
  return (
    <InnerBox>
      <MuiTypography> Your Products</MuiTypography>
      <ol>
        {props.boxProps.map((box) => (
          <li>
            {box.name}- {box.price}
          </li>
        ))}
      </ol>
      <Typography>Total: {getTotalPrice()}</Typography>
      <EndBox>
        <MuiButton
          variant={"contained"}
          text={"Pay"}
          sx={{ backgroundColor: "blue", color: "white" }}
          onClick={() => {
            props.onBuy();
          }}
        ></MuiButton>
        <MuiButton
          variant={"outlined"}
          text={"Cancel"}
          sx={{ backgroundColor: "white", color: "black" }}
          onClick={props.onCancel}
        ></MuiButton>
      </EndBox>
    </InnerBox>
  );
};

export default OpenModal;
