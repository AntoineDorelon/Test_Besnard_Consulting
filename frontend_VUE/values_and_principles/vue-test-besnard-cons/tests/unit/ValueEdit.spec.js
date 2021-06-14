import { mount } from "@vue/test-utils";
import ValueEdit from "../../src/components/ValueEdit";

describe("ValueEdit", () => {
  const value = { id: 1, title: "test-value" };
  const wrapper = mount(ValueEdit, {
    propsData: { value },
  });

  test("contains the value title in 'Camel case' when a value is passed", () => {
    expect(wrapper.html()).toContain(
      value.title.charAt(0).toUpperCase() + value.title.slice(1)
    );
  });

  test("contains the value in the placeholder", () => {
    // expect(wrapper.html()).toMatchSnapshot();
    const placeholderValue = wrapper.find("input").element.value;
    expect(placeholderValue).toBe("test-value");
  });

  test("calls saveValue() method when the button is clicked", async () => {
    const button = wrapper.find("button");
    const spy = jest.spyOn(wrapper.vm, "saveValue");
    await button.trigger("click");
    expect(spy).toHaveBeenCalled();
  });
});
