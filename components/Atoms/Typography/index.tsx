import { Typography, TypographyProps } from "@mui/material";

interface TypographyProp extends TypographyProps {
  children: any;
}
export const MuiTypography = (props: TypographyProp) => {
  return (
    <Typography variant={props.variant} {...props}>
      {props.children}
    </Typography>
  );
};
