<template>
    <div class="rental-car-list">
        <div v-for="car in cars" :key="car.id" class="rental-car">
            <img :src="require(`@/assets/${car.image}`)" alt="Car Image">
            <div class="details">
                <h3>{{ car.make }} {{ car.model }}</h3>
                <p>{{ car.year }}</p>
                <p>{{ car.price }}.00$</p>
            </div>
            <div class="features">
                <img v-if="car.isElectric" src='../assets/lightning.png' class="icon">
                <img v-if="car.isAllWheelDrive" src='../assets/wheels.png' class="icon">
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'CarListing',
    data() {
        return {
            cars: [
                {
                    id: 1,
                    make: 'Toyota',
                    model: 'Corolla',
                    year: 2020,
                    price: 50.00,
                    image: 'toyota_corolla.png',
                    isElectric:true,
                    isAllWheelDrive: true
                },
                {
                    id: 3,
                    make: 'Toyota',
                    model: 'Corolla',
                    year: 2020,
                    price: 50.00,
                    image: 'toyota_corolla.png',
                    isElectric:false,
                    isAllWheelDrive: false
                }

            ]
        }
    }
}
</script>

<style scoped>
.rental-car-list {
    display: flex;
    flex-wrap: wrap;
}
.rental-car {
    margin: 10px;
    padding: 10px;
    border: 1px solid black;
    border-radius: 5px;
    width: 300px;
    position: relative;
}
.rental-car img{
    width:100%;
    height: auto;
    border-radius: 5px;
}
.details p:last-child {
    position: absolute  ;
    margin-top: 10px;
    bottom: 5px;
    right: 20px;
    font: bold 20px Arial, sans-serif;

    
}
.features{
    display: flex;
    align-items: end;
}
.features img{
    height: 50px;
    width:50px ;
    margin-right: 10px;
}
</style>

