import styled from "@emotion/styled";

import React, { useEffect, useState } from "react";

import { Badge } from "@mui/material";
import ShoppingCartIcon from "@mui/icons-material/ShoppingCart";
import axios from "axios";
import MuiButton from "../../Atoms/Button";
import { MuiTypography } from "../../Atoms/Typography";
import OpenModal from "../../molecule/OpenModal";
import Input from "../../Atoms/TextField";
import SearchIcon from "@mui/icons-material/Search";
import IconComponent from "../../Atoms/Icon";
const OuterBox = styled("div")(() => ({
  marginTop: "200px",
  alignItems: "center",
  display: "flex",
  gap: "20px",
  flexDirection: "column",
}));

const DownBox = styled("div")(() => ({
  display: "flex",
  width: "70%",
  height: "140px",
  alignItems: "center",
  gap: "20px",
  marginLeft: "40%",
  marginTop: "90px",
}));

const InnerBox = styled("div")(() => ({
  height: "120px",
  width: "180px",
  border: "1px solid black",
  alignItems: "center",
  padding: "20px",
  gap: "20px",
}));

const StartBox = styled("div")(() => ({
  width: "500px",
  gap: "25px",
  display: "flex",
  flexDirection: "row",
  marginLeft: "20%",
}));
const CartIcon = styled(Badge)(({ theme }) => ({
  "& .MuiBadge-badge": {
    right: -8,
    top: 10,
    padding: "0 4px",
  },
}));

interface BoxProp {
  name: String;
  price: number;
}

const BuyCard = () => {
  const [modal, setModal] = useState(false);
  const [buyData, setBuyData] = useState<BoxProp[]>([]);
  const [search, setSearch] = useState("");
  const [data, setData] = useState<any[]>([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get("http://localhost:3000/data");
        setData(response.data);
      } catch (error) {
        console.error("Error fetching data:", error);
      }
    };

    fetchData();
  }, []);

  const handleClick = (name: string, price: number) => {
    setBuyData((prevBuyData) => [
      ...prevBuyData,
      {
        name: name,
        price: price,
      },
    ]);
  };
  const handleBuy = () => {
    setModal(true);
  };
  const filteredData = data.filter((box: any) =>
    box.name.toLowerCase().includes(search.toLowerCase())
  );

  return (
    <OuterBox>
      <StartBox>
        <p>Ecommerece App</p>
        <Input
          variant={"outlined"}
          placeholder={"Search"}
          type={"text"}
          onChange={(e) => setSearch(e.target.value)}
          textFieldIcon={
            <IconComponent icon={<SearchIcon />} alt="Search Icon" />
          }
        />
        <CartIcon badgeContent={buyData.length} color="primary">
          <ShoppingCartIcon />
        </CartIcon>
      </StartBox>
      <React.Fragment>
        <DownBox>
          {filteredData.map((box: any) => {
            return (
              <InnerBox>
                <MuiTypography>name:{box.name}</MuiTypography>

                <MuiTypography>manfacture:{box.manufacturer}</MuiTypography>

                <MuiTypography>Price:{box.price}</MuiTypography>
                <MuiButton
                  variant={"contained"}
                  text={"Add"}
                  sx={{ backgroundColor: "blue", color: "white" }}
                  onClick={() => {
                    handleClick(box.name, box.price);
                  }}
                ></MuiButton>
              </InnerBox>
            );
          })}
        </DownBox>

        <MuiButton
          variant={"contained"}
          text={"Buy Now"}
          sx={{ backgroundColor: "green", color: "white", marginTop: "30px" }}
          onClick={() => {
            handleBuy();
          }}
        ></MuiButton>
        {modal && (
          <OpenModal
            boxProps={buyData}
            onCancel={function (): void {
              setModal(false);
            }}
            onBuy={function (): void {
              setModal(false);
            }}
          />
        )}
      </React.Fragment>
    </OuterBox>
  );
};

export default BuyCard;
