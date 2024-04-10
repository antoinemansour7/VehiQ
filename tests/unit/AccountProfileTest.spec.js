import { mount } from '@vue/test-utils'
import AccountProfile from '@views/AccountProfile.vue'
import axios from 'axios'

// Mock Axios
jest.mock('axios', () => ({
  get: jest.fn(),
  delete: jest.fn(),
}))

describe('AccountProfile', () => {
  let wrapper

  beforeEach(() => {
    // Mock the response of axios.get
    axios.get.mockResolvedValue({
      data: [
        {
          id: 1,
          car_details: { make: 'Toyota', model: 'Corolla' },
          start_date: '2024-04-10',
          end_date: '2024-04-15',
          reservation_date: '2024-04-01',
          pickup_location: 'Location A',
          dropoff_location: 'Location B',
          user_details: { user: 'JohnDoe' }
        }
      ]
    })

    wrapper = mount(AccountProfile)
  })

  afterEach(() => {
    jest.clearAllMocks()
  })

  it('updates information and retains after saving', async () => {
    // Wait for Vue to update DOM after axios response
    await wrapper.vm.$nextTick()

    // Click edit button
    await wrapper.find('.save-button').trigger('click')

    // Simulate changing the username
    const newUsername = 'JaneDoe'
    await wrapper.find('#username').setValue(newUsername)

    // Assert that the username in the form data is updated
    expect(wrapper.vm.formData.username).toBe(newUsername)

    // Save profile
    await wrapper.find('.save-button').trigger('click')

    // Wait for Vue to update DOM after saving
    await wrapper.vm.$nextTick()

    // Check if the username displayed matches the updated username
    expect(wrapper.find('#username').element.value).toBe(newUsername)
  })
})
