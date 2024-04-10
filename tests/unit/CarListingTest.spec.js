import { mount } from '@vue/test-utils';
import CarListing from '@views/CarListing.vue';
import axios from 'axios';

// Mock axios
jest.mock('axios', () => ({
  get: jest.fn(),
  delete: jest.fn(),
}));

describe('CarListing', () => {
  let wrapper;

  beforeEach(() => {

    global.alert = jest.fn();
    // Mock the response data for axios.get
    axios.get.mockResolvedValue({
      data: [
        {
          id: 1,
          make: 'Toyota',
          model: 'Corolla',
          year: 2020,
          price: 15000,
          is_electric: false,
          is_all_wheel_drive: true,
        },
        // Add more mock data as needed
      ],
    });

    // Mount the component
    wrapper = mount(CarListing);
  });

  afterEach(() => {
    // Clear the mocked axios functions
    global.alert.mockClear();
    jest.clearAllMocks();
  });

  it('displays a list of cars', async () => {
    // Wait for axios.get to be called
    await expect(axios.get).toHaveBeenCalledTimes(1);

    // Check if the cars are rendered
    const cars = wrapper.findAll('.rental-car');
    expect(cars.length).toBe(1); // Adjust based on the mock data
  });

  it('deletes a car when delete button is clicked', async () => {
    // Mock the successful response for axios.delete
    axios.delete.mockResolvedValueOnce();

    // Find the delete button and trigger a click event
    await wrapper.find('.button-looking.small-button:nth-child(1)').trigger('click');

    // Wait for axios.delete to be called
    await expect(axios.delete).toHaveBeenCalledWith('http://127.0.0.1:8000/vehicles/cars/1/');

    // Check if the car is removed from the list
    const carsAfterDeletion = wrapper.findAll('.rental-car');
    expect(carsAfterDeletion.length).toBe(0);
  });

  // Add more test cases for other functionalities as needed
});
