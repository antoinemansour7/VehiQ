import { shallowMount } from '@vue/test-utils';
import LogIn from '@views/LogIn.vue';

describe('LogIn.vue', () => {
  it('renders correctly', () => {
    const wrapper = shallowMount(LogIn);
    expect(wrapper.exists()).toBe(true);
  });

  it('initializes with logInAdmin tab active', () => {
    const wrapper = shallowMount(LogIn);
    const activeTab = wrapper.vm.activeTab;
    expect(activeTab).toBe('logInAdmin');
  });

  it('switches to logInUser tab when clicked', async () => {
    const wrapper = shallowMount(LogIn);
    await wrapper.find('.tab:nth-child(2)').trigger('click');
    const activeTab = wrapper.vm.activeTab;
    expect(activeTab).toBe('logInUser');
  });

  it('resets form data after logInAsAdmin method is called', async () => {
    const wrapper = shallowMount(LogIn);
    wrapper.setData({ formData: { username: 'admin', password: 'password' } });
    await wrapper.vm.logInAsAdmin();
    const formData = wrapper.vm.formData;
    expect(formData.username).toBe('');
    expect(formData.password).toBe('');
  });

  it('resets form data after logInAsUser method is called', async () => {
    const wrapper = shallowMount(LogIn);
    wrapper.setData({ formData: { username: 'user', password: 'password' } });
    await wrapper.vm.logInAsUser();
    const formData = wrapper.vm.formData;
    expect(formData.username).toBe('');
    expect(formData.password).toBe('');
  });
});
