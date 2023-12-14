import { useDispatch, useSelector } from "react-redux";
import { useHistory } from "react-router";
import authSlice from "../store/slices/auth";
// import useSWR from 'swr';
// import { fetcher } from "../utils/axios";
// import { UserResponse } from "../utils/types";
import { RootState } from "../store";
import {Container, Box, CssBaseline, Button} from '@mui/material';
import GenerateForm from './GenerateForm'

const Work = () => {
  const account = useSelector((state: RootState) => state.auth.account);
  const dispatch = useDispatch();
  const history = useHistory();
  // @ts-ignore
  const userId = account?.id;
  // const user = useSWR<UserResponse>(`/user/${userId}/`, fetcher)

  const handleLogout = () => {
    dispatch(authSlice.actions.setLogout());
    history.push("/login");
  };

  return (
    <Container component="main" maxWidth="xs">
      <CssBaseline />
      <Box
        sx={{
          marginTop: 8,
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center',
        }}
      >
        <Button
          onClick={handleLogout}
          variant="contained"
          sx={{ mt: 3, mb: 2 }}
        >
          Log out
        </Button>
        <GenerateForm userId={userId}/>
      </Box>
    </Container>
  )
};

export default Work;
