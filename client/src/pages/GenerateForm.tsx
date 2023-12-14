import AutoModeIcon from '@mui/icons-material/AutoMode';
import { Typography, Avatar, Button, Box, TextField } from '@mui/material';


export default function GenerateForm(props: any) {
    const userId = props.userId

    const handleSubmit = (event: any) => {
        event.preventDefault();
        console.log(userId);
        // send file here
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
            <Box component="form" onSubmit={handleSubmit} noValidate sx={{ mt: 1 }}>
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
        </Box>
    )
}