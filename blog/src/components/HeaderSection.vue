<template>
    <header>
        <div class="headerContent">
            <div class="centerItems">
                <h1 class="companyName">{{ msg }}</h1> <!--Link to home page-->
                <img class="logo" alt="VehiQ logo" src="../assets/VEHIQ_logo.png"> <!--Link to home page-->
            </div>
        </div>
        <div class="buttons">
            <img class="profile-button" alt="Profile button" src="../assets/Default_Profile.png" @click="openProfile">
            <img class="nav-button" alt="Navigation button" src="../assets/Nav_Button.png" @click="toggleNavbar">
        </div>
        <nav v-if="showNavbar">
            <!-- links -->
        </nav>
    </header>
</template>

<script>
    export default {
        name: 'HeaderSection',
        data() {
            return {
                showNavbar: false
            };
        },
        methods: {
            toggleNavbar() {
                this.showNavbar = !this.showNavbar;
            },
            openProfile() {
                // Add logic to open profile
            }
        },
        props: {
            msg: String
        }
    }
</script>

<style>
    header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 20px;
        background-color: #3f3f3f;
    }

    .centerItems {
        display: flex;
        align-items: center;
    }

    .headerContent {
        flex-grow: 1;
        display: flex;
        justify-content: center;
    }

    .buttons {
        display: flex;
        align-items: center;
    }

    .companyName{
        color:rgb(228, 223, 228);
    }
    .logo {
        width: 100px;
        height: auto;
        margin-right: 10px;
    }

    .nav-button, .profile-button {
        width: 40px;
        cursor: pointer;
    }

    .profile-button {
        margin-right: 10px;
    }

    nav {
        /* Add styles for the navigation bar */
    }
</style>