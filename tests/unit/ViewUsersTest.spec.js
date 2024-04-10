import { shallowMount } from '@vue/test-utils';
import ViewUsers from '@views/ViewUsers.vue';

jest.mock('axios', () => ({
  get: jest.fn(),
  delete: jest.fn()
}));

describe('ViewUsers.vue', () => {
  afterEach(() => {
    jest.clearAllMocks(); // Clear mock calls after each test
  });

  it('fetches users data on mount', async () => {
    const userData = [
      { id: 1, user: 'User A', email: 'userA@example.com', first_name: 'John', is_staff: false },
      { id: 2, user: 'User B', email: 'userB@example.com', first_name: 'Jane', is_staff: true }
    ];
    // Mock axios.get to return resolved promise with the user data
    axios.get.mockResolvedValueOnce({ data: userData });

    const wrapper = shallowMount(ViewUsers);

    // Wait for the next tick of the event loop to allow the promise to resolve
    await wrapper.vm.$nextTick();

    // Assert that axios.get was called with the correct URL
    expect(axios.get).toHaveBeenCalledWith('http://127.0.0.1:8000/accounts/user/');

    // Assert that the component's users data is set correctly
    expect(wrapper.vm.users).toEqual(userData);
  });

  it('deletes user on button click', async () => {
    const userData = [
      { id: 1, user: 'User A', email: 'userA@example.com', first_name: 'John', is_staff: false },
      { id: 2, user: 'User B', email: 'userB@example.com', first_name: 'Jane', is_staff: true }
    ];
    axios.get.mockResolvedValueOnce({ data: userData });

    const wrapper = shallowMount(ViewUsers);

    await wrapper.vm.$nextTick();

    // Mock axios.delete to return resolved promise
    axios.delete.mockResolvedValueOnce();

    // Simulate button click to delete a user
    wrapper.find('button').trigger('click');

    await wrapper.vm.$nextTick();

    // Assert that axios.delete was called with the correct URL
    expect(axios.delete).toHaveBeenCalledWith('http://127.0.0.1:8000/accounts/user/1/');

    // Assert that the user is removed from the component's users data
    expect(wrapper.vm.users.length).toBe(userData.length - 1);
  });
});
