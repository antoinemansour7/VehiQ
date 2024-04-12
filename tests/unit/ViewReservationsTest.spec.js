import { mount } from '@vue/test-utils';
import HomeView from '@/views/HomeView.vue'; // Adjust the path as per your project structure
import axios from 'axios';

// Mock axios
jest.mock('axios');

describe('HomeView.vue', () => {
  it('renders without errors', () => {
    // Mount the component
    const wrapper = mount(HomeView);

    // Check if the component exists
    expect(wrapper.exists()).toBe(true);

    // Check if the h1 element exists and contains the correct text
    expect(wrapper.find('h1').text()).toBe('Available Reservations');
  });

  it('fetches reservations on mount', async () => {
    // Mock response data
    const mockResponse = [
      {
        id: 1,
        car_details: { make: 'Make A', model: 'Model A' },
        user_details: { user: 'User A' },
        start_date: '2024-04-15',
        end_date: '2024-04-20',
        reservation_date: '2024-04-10',
        pickup_location: 'Location A',
        dropoff_location: 'Location B'
      },
      {
        id: 2,
        car_details: { make: 'Make B', model: 'Model B' },
        user_details: { user: 'User B' },
        start_date: '2024-04-25',
        end_date: '2024-04-30',
        reservation_date: '2024-04-20',
        pickup_location: 'Location C',
        dropoff_location: 'Location D'
      }
    ];

    // Mock axios.get to return a promise with reservations data
    axios.get.mockResolvedValueOnce({ data: mockResponse });

    // Mount the component
    const wrapper = mount(HomeView);

    // Wait for next tick to ensure promises resolve
    await wrapper.vm.$nextTick();

    // Check if axios.get was called with the correct URL
    expect(axios.get).toHaveBeenCalledWith('http://127.0.0.1:8000/accounts/reservations/');

    // Check if reservations are set correctly after the call
    expect(wrapper.vm.reservations).toEqual(mockResponse);
  });
});
