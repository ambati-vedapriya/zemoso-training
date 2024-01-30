import React from "react";
import { SvgIconProps } from "@mui/material/SvgIcon";

interface IIconProps {
  icon: React.ReactElement<SvgIconProps>;
  alt: string;
  style?: React.CSSProperties;
}

const IconComponent = ({ icon, alt }: IIconProps) => {
  return (
    <span aria-label={alt} style={{ cursor: "pointer" }}>
      {icon}
    </span>
  );
};

export default IconComponent;
