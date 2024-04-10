import { shallowMount } from '@vue/test-utils';
import Reservations from '@views/Reservations.vue';
import axios from 'axios';

jest.mock('axios', () => ({
  get: jest.fn(),
}));

describe('Reservations.vue', () => {
  afterEach(() => {
    jest.clearAllMocks(); // Clear mocks after each test
  });

  it('renders without errors', () => {
    const wrapper = shallowMount(Reservations);
    expect(wrapper.exists()).toBe(true);
  });

  // it('updates reservations when getAllReservations method is called', async () => {
  //   const mockResponse = {
  //     data: [
  //       { id: 1, car_name: 'Car A', profile_name: 'User A', start_date: '2024-04-15', end_date: '2024-04-20', reservation_date: '2024-04-10' },
  //       { id: 2, car_name: 'Car B', profile_name: 'User A', start_date: '2024-04-25', end_date: '2024-04-30', reservation_date: '2024-04-20' }
  //     ]
  //   };
  //   axios.get.mockResolvedValueOnce({ data: { id: 123 } }); // Mock user response
  //   axios.get.mockResolvedValueOnce(mockResponse); // Mock reservation response

  //   const wrapper = shallowMount(Reservations);
  //   wrapper.vm.getAllReservations();

  //   expect(wrapper.vm.reservations).toEqual(mockResponse.data);
  // });
});
