import { mount } from '@vue/test-utils';
import HomeView from '@views/HomeView.vue';

describe('HomeView', () => {
  let wrapper;

  beforeEach(() => {
    wrapper = mount(HomeView);
  });

  afterEach(() => {
    wrapper.destroy();
  });

  it('renders correctly', () => {
    expect(wrapper.exists()).toBe(true);
  });

  it('renders the welcome message', () => {
    const welcomeMessage = wrapper.find('.home-container h1');
    expect(welcomeMessage.exists()).toBe(true);
    expect(welcomeMessage.text()).toBe('Welcome to VehiQ');
  });

  it('renders the VehiQ logo', () => {
    const logo = wrapper.find('.home-container img.VehiQLogo');
    expect(logo.exists()).toBe(true);
    expect(logo.attributes('src')).toBe('@/assets/VEHIQ_logo.png');
  });

  it('renders the welcome text', () => {
    const welcomeText = wrapper.find('.home-container .welcome-text');
    expect(welcomeText.exists()).toBe(true);
    // Add more specific assertions for the welcome text content if needed
  });

  it('renders the fireworks', () => {
    const fireworks = wrapper.findAll('.home-container .firework');
    expect(fireworks.length).toBe(2); // Expecting two fireworks elements
  });
});
