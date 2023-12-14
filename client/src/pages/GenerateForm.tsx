import AutoModeIcon from '@mui/icons-material/AutoMode';
import { Typography, Avatar, Button, Box, TextField } from '@mui/material';
import * as Yup from "yup";
import { useFormik } from "formik";
import axios from "axios";

export default function GenerateForm(props: any) {
    const userId = props.userId

    const formik = useFormik({
        initialValues: {
            email: "",
        },
        onSubmit: (values) => {
            axios
                .post(`${process.env.REACT_APP_API_URL}get_answer/`, { userId: userId, ...values })
        },
        validationSchema: Yup.object({
            email: Yup.string().trim(),
        }),
    });


    const handleGetHistory = () => {
        // 
    }

    return (
        <Box
            sx={{
                marginTop: 8,
                display: 'flex',
                flexDirection: 'column',
                alignItems: 'center',
            }}
        >
            <Avatar sx={{ m: 1, bgcolor: 'secondary.main' }}>
                <AutoModeIcon />
            </Avatar>
            <Typography component="h1" variant="h5">
                Generate NBO
            </Typography>
            <Box component="form" onSubmit={formik.handleSubmit} noValidate sx={{ mt: 1 }}>
                <TextField
                    margin="normal"
                    required
                    fullWidth
                    hidden={true}
                    name="file"
                    type="file"
                />
                <Button
                    type="submit"
                    fullWidth
                    variant="contained"
                    sx={{ mt: 3, mb: 2 }}
                >
                    Generate
                </Button>
            </Box>
            <Button
                onClick={handleGetHistory}
                variant="contained"
                sx={{ mt: 3, mb: 2 }}
            >
                Download json history
            </Button>
        </Box>
    )
}