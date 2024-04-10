import { mount } from '@vue/test-utils';
import CreateCarForm from '@/views/CreateCarForm.vue';
import axios from 'axios';

jest.mock('axios', () => ({
  post: jest.fn(),
}));

describe('CreateCarForm', () => {
  let wrapper;

  beforeEach(() => {
    wrapper = mount(CreateCarForm);
  });

  afterEach(() => {
    wrapper.destroy();
  });

  it('submits the form successfully', async () => {
    // Fill in form fields
    await wrapper.setData({
      car: {
        make: 'Toyota',
        model: 'Camry',
        year: 2022,
        price: 25000,
        electric: true,
        allWheelDrive: false,
        image: null,
      },
    });

    // Mock axios post response
    axios.post.mockResolvedValueOnce({ data: { id: 1 } });

    // Spy on console.log
    const consoleSpy = jest.spyOn(console, 'log');

    // Trigger form submission
    await wrapper.find('form').trigger('submit.prevent');

    // Assert that axios post was called with correct data
    expect(axios.post).toHaveBeenCalledWith('http://127.0.0.1:8000/vehicles/cars/', {
      make: 'Toyota',
      model: 'Camry',
      year: 2022,
      price: 25000,
      electric: true,
      allWheelDrive: false,
      image: null,
    });

    // Assert success message
    expect(consoleSpy).toHaveBeenCalledWith('Car added successfully', { id: 1 });

    // Assert form reset
    expect(wrapper.vm.car).toEqual({
      make: '',
      model: '',
      year: null,
      price: null,
      electric: false,
      allWheelDrive: false,
      image: null,
    });

    // Restore the original console.log function
    consoleSpy.mockRestore();
  });
});
