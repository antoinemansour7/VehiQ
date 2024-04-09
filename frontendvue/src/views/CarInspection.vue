<template>
    <h2>Car Inspection Form for car : (car id and name)</h2>
    <h3>Returned by : (user name)</h3> 
    <div id="checkOutInfo">
        This is a form that checks for any damages on the car. 
        The initial amount is what will be deducted if all damages are found. As you check boxes, 
        the amount will be set to the appropriate deduction. <br><br>
          
        Please inform the client that if any damage is found, they will be charged for the repair. The amount will be deducted from their deposit.<br> <br> 
        <b>Please check the boxes that apply.</b>
    </div>

    <div class="car-inspection-form">              
        <form @submit.prevent="submitForm">
            <div class="form-group">
                <div class="checkbox-group">
                    <label class="myCheckBox">
                        <input type="checkbox" v-model="damageDescriptions.wheelsPressure">
                        Wheels Pressure Okay
                    </label>
                    <label class="myCheckBox">
                        <input type="checkbox" v-model="damageDescriptions.ACWorking">
                        AC Working
                    </label>
                    <label class="myCheckBox">
                        <input type="checkbox" v-model="damageDescriptions.spareTirePresent">
                        Spare Tire Present
                    </label>
                    <label class="myCheckBox">
                        <input type="checkbox" v-model="damageDescriptions.checkEngine">
                        Check Engine off
                    </label>
                    <label class="myCheckBox">
                        <input type="checkbox" v-model="damageDescriptions.oilLevels">
                        Oil Levels sufficient
                    </label>
                    <label class="myCheckBox"> 
                        <input type="checkbox" v-model="damageDescriptions.washerFluids">
                        Washer Fluids full
                    </label>
                    <label class="myCheckBox">
                        <input type="checkbox" v-model="damageDescriptions.heatingWorking">
                        Heating Working
                    </label>
                </div>
            </div>
            <button type="submit">Submit</button>
            <p>Total Deduction: {{ calculateDeduction() }}</p>
        </form>
    </div>
</template>

<script>
export default {
    data() {
        return {
            carMake: '',
            carModel: '',
            damageDescriptions: {
                wheelsPressure: false,
                ACWorking: false,
                spareTirePresent: false,
                checkEngine: false,
                oilLevels: false,
                washerFluids: false,
                heatingWorking: false,
            },
        };
    },
    methods: {
        submitForm() {
            console.log("Form submitted with data:", this.carMake, this.carModel, this.damageDescriptions);
        },
        calculateDeduction() {
            let deduction = 0;
            if (!this.damageDescriptions.wheelsPressure) {
                deduction += 50; 
            }
            if (!this.damageDescriptions.ACWorking) {
                deduction += 100; 
            }
            if (!this.damageDescriptions.spareTirePresent) {
                deduction += 75; 
            }
            if(!this.damageDescriptions.checkEngine){
                deduction += 100; 
            }
            if(!this.damageDescriptions.oilLevels){
                deduction += 50; 
            }
            if(!this.damageDescriptions.washerFluids){
                deduction += 25; 
            }
            if(!this.damageDescriptions.heatingWorking){
                deduction += 75; 
            }
            return deduction;
        }
    }
};
</script>

<style scoped>

.car-inspection-form {
    max-width: 600px;
    margin: 0 auto;
    padding: 20px;
    border-radius: 8px;
    background-color: #f1eff3; /* Light purple background */
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}
#checkOutInfo{
    max-width: 600px;
    margin: 0 auto;
    padding: 20px;
    border-radius: 8px;
    background-color: #e3d7ef; /* Light purple background */
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    text-align: left;
    margin-bottom: 10px;
}


.form-group {
    margin-bottom: 20px;
}

label {
    display: block;
    font-weight: bold;
    color: #6A0DAD; /* Purple color */
}

input[type="checkbox"] {
    margin-right: 5px;
}

button {
    padding: 10px 20px;
    background-color: #6A0DAD; /* Purple color */
    color: #fff;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}

p {
    color: #6A0DAD; /* Purple color */
    font-weight: bold;
}

.myCheckBox{
    margin: 10px;
}

</style>
